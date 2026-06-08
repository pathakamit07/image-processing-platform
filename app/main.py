from fastapi import FastAPI

from app.api.jobs import router as jobs_router
from app.api.health import router as health_router

app = FastAPI(
    title="Image Processing Platform",
    version="1.0.0"
)

app.include_router(jobs_router)
app.include_router(health_router)