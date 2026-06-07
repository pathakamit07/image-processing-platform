from fastapi import FastAPI
from app.config import APP_NAME, VERSION
from app.api.tasks import router as task_router
from app.middleware.request_logger import RequestLoggerMiddleware

app = FastAPI(title=APP_NAME, version=VERSION)

app.add_middleware(RequestLoggerMiddleware)
app.include_router(task_router)

@app.get("/health")
def health():
    return {"status": "UP"}
