from fastapi import APIRouter

from app.models.schemas import (
    JobRequest,
    JobResponse
)

from app.services.sqs_service import (
    sqs_service
)


router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"]
)


@router.post(
    "",
    response_model=JobResponse
)
def create_job(
    payload: JobRequest
):

    sqs_service.send_message({

        "jobId": payload.jobId,

        "prompt": payload.prompt
    })

    return {

        "success": True,

        "message":
        "Job submitted successfully",

        "jobId": payload.jobId
    }