import boto3

from botocore.exceptions import ClientError

from app.config import settings
from app.utils.helpers import current_timestamp


dynamodb = boto3.resource(
    "dynamodb",
    region_name=settings.AWS_REGION
)


lock_table = dynamodb.Table(
    settings.DYNAMODB_LOCK_TABLE
)

metadata_table = dynamodb.Table(
    settings.DYNAMODB_METADATA_TABLE
)


class DynamoDBService:

    def acquire_lock(
        self,
        job_id,
        owner,
        ttl
    ):

        try:

            lock_table.put_item(

                Item={
                    "jobId": job_id,
                    "owner": owner,
                    "createdAt":
                    current_timestamp(),
                    "ttl": ttl
                },

                ConditionExpression=
                "attribute_not_exists(jobId)"
            )

            return True

        except ClientError:

            return False

    def release_lock(
        self,
        job_id
    ):

        lock_table.delete_item(
            Key={
                "jobId": job_id
            }
        )

    def store_metadata(
        self,
        data
    ):

        metadata_table.put_item(
            Item=data
        )

    def get_metadata(
        self,
        job_id
    ):

        response = metadata_table.get_item(
            Key={
                "jobId": job_id
            }
        )

        return response.get("Item")


dynamodb_service = DynamoDBService()