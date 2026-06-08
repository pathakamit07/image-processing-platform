from app.config import settings

from app.utils.helpers import (
    current_timestamp
)

from app.services.dynamodb_service import (
    dynamodb_service
)


class LockService:

    def acquire(
        self,
        job_id,
        owner
    ):

        ttl = (
            current_timestamp()
            +
            settings.LOCK_TTL_SECONDS
        )

        return dynamodb_service.acquire_lock(
            job_id,
            owner,
            ttl
        )

    def release(
        self,
        job_id
    ):

        dynamodb_service.release_lock(
            job_id
        )


lock_service = LockService()