import json

from app.services.sqs_service import (
    sqs_service
)

from app.services.lock_service import (
    lock_service
)

from app.services.image_service import (
    image_service
)

from app.services.s3_service import (
    s3_service
)

from app.services.metadata_service import (
    metadata_service
)

from app.services.cloudwatch_service import (
    cloudwatch_service
)

from app.workers.visibility_heartbeat import (
    VisibilityHeartbeat
)

from app.utils.helpers import (
    generate_s3_key,
    generate_worker_id,
    current_timestamp
)

from app.utils.logger import log_json


worker_id = generate_worker_id()


def process_job():

    while True:

        messages = (
            sqs_service.receive_messages()
        )

        if not messages:

            continue

        for message in messages:

            receipt_handle = (
                message["ReceiptHandle"]
            )

            body = json.loads(
                message["Body"]
            )

            job_id = body["jobId"]

            prompt = body["prompt"]

            existing = (
                metadata_service.get_record(
                    job_id
                )
            )

            if existing:

                log_json({

                    "jobId": job_id,

                    "status":
                    "already_completed"
                })

                sqs_service.delete_message(
                    receipt_handle
                )

                continue

            lock = lock_service.acquire(
                job_id,
                worker_id
            )

            if not lock:

                log_json({

                    "jobId": job_id,

                    "status":
                    "lock_failed"
                })

                cloudwatch_service.put_metric(
                    "LockFailures",
                    1
                )

                continue

            heartbeat = (
                VisibilityHeartbeat(
                    receipt_handle
                )
            )

            heartbeat.start()

            try:

                log_json({

                    "jobId": job_id,

                    "status":
                    "processing"
                })

                image_path = (
                    image_service.generate_image(
                        job_id,
                        prompt
                    )
                )

                s3_key = (
                    generate_s3_key(job_id)
                )

                exists = (
                    s3_service.object_exists(
                        s3_key
                    )
                )

                if exists:

                    log_json({

                        "jobId": job_id,

                        "status":
                        "already_uploaded"
                    })

                else:

                    s3_path = (
                        s3_service.upload_file(
                            image_path,
                            s3_key
                        )
                    )

                    metadata_service.create_record({

                        "jobId": job_id,

                        "status": "COMPLETED",

                        "s3Path": s3_path,

                        "completedAt":
                        current_timestamp()
                    })

                sqs_service.delete_message(
                    receipt_handle
                )

                log_json({

                    "jobId": job_id,

                    "status":
                    "completed"
                })

                cloudwatch_service.put_metric(
                    "JobsProcessed",
                    1
                )

            except Exception as error:

                log_json({

                    "jobId": job_id,

                    "status": "failed",

                    "error": str(error)
                })

                cloudwatch_service.put_metric(
                    "JobsFailed",
                    1
                )

            finally:

                heartbeat.stop()

                lock_service.release(
                    job_id
                )


if __name__ == "__main__":

    process_job()