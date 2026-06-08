import boto3

from botocore.exceptions import ClientError

from app.config import settings


s3 = boto3.client(
    "s3",
    region_name=settings.AWS_REGION
)


class S3Service:

    def object_exists(
        self,
        key
    ):

        try:

            s3.head_object(
                Bucket=settings.S3_BUCKET_NAME,
                Key=key
            )

            return True

        except ClientError:

            return False

    def upload_file(
        self,
        local_file,
        key
    ):

        s3.upload_file(
            local_file,
            settings.S3_BUCKET_NAME,
            key
        )

        return (
            f"s3://"
            f"{settings.S3_BUCKET_NAME}/"
            f"{key}"
        )


s3_service = S3Service()