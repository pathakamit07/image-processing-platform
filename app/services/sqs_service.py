import json
import boto3

from app.config import settings


sqs = boto3.client(
    "sqs",
    region_name=settings.AWS_REGION
)


class SQSService:

    def send_message(
        self,
        payload
    ):

        return sqs.send_message(
            QueueUrl=settings.SQS_QUEUE_URL,
            MessageBody=json.dumps(payload)
        )

    def receive_messages(self):

        response = sqs.receive_message(
            QueueUrl=settings.SQS_QUEUE_URL,
            MaxNumberOfMessages=1,
            WaitTimeSeconds=20,
            VisibilityTimeout=300
        )

        return response.get(
            "Messages",
            []
        )

    def delete_message(
        self,
        receipt_handle
    ):

        sqs.delete_message(
            QueueUrl=settings.SQS_QUEUE_URL,
            ReceiptHandle=receipt_handle
        )

    def extend_visibility(
        self,
        receipt_handle,
        timeout=300
    ):

        sqs.change_message_visibility(
            QueueUrl=settings.SQS_QUEUE_URL,
            ReceiptHandle=receipt_handle,
            VisibilityTimeout=timeout
        )


sqs_service = SQSService()