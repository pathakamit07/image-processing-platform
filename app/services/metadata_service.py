from app.services.dynamodb_service import (
    dynamodb_service
)


class MetadataService:

    def create_record(
        self,
        data
    ):

        dynamodb_service.store_metadata(
            data
        )

    def get_record(
        self,
        job_id
    ):

        return dynamodb_service.get_metadata(
            job_id
        )


metadata_service = MetadataService()