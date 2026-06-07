from fastapi import APIRouter
from app.models.schemas import TaskCreate, TaskUpdate
from app.services.task_service import task_service
from app.utils.exceptions import task_not_found

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post("")
def create_task(task: TaskCreate):
    return task_service.create_task(task)

@router.get("")
def get_tasks():
    return task_service.get_all_tasks()

@router.get("/{task_id}")
def get_task(task_id: str):
    task = task_service.get_task(task_id)
    if not task:
        task_not_found()
    return task

@router.put("/{task_id}")
def update_task(task_id: str, task: TaskUpdate):
    result = task_service.update_task(task_id, task)
    if not result:
        task_not_found()
    return result

@router.delete("/{task_id}")
def delete_task(task_id: str):
    result = task_service.delete_task(task_id)
    if not result:
        task_not_found()
    return {"message": "Task deleted successfully"}
