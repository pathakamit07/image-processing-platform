import os


class Settings:

    APP_NAME = "Image Processing Platform"

    AWS_REGION = os.getenv(
        "AWS_REGION",
        "us-east-1"
    )

    SQS_QUEUE_URL = os.getenv(
        "SQS_QUEUE_URL"
    )

    S3_BUCKET_NAME = os.getenv(
        "S3_BUCKET_NAME"
    )

    DYNAMODB_LOCK_TABLE = os.getenv(
        "DYNAMODB_LOCK_TABLE",
        "job-locks"
    )

    DYNAMODB_METADATA_TABLE = os.getenv(
        "DYNAMODB_METADATA_TABLE",
        "job-metadata"
    )

    VISIBILITY_TIMEOUT = 300

    LOCK_TTL_SECONDS = 1800


settings = Settings()