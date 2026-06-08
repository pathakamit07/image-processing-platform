from pydantic import BaseModel
from typing import Optional


class JobRequest(BaseModel):

    jobId: str

    prompt: str


class JobResponse(BaseModel):

    success: bool

    message: str

    jobId: str


class MetadataRecord(BaseModel):

    jobId: str

    status: str

    s3Path: Optional[str] = None