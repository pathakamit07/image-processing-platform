from fastapi import HTTPException
def task_not_found():
    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )
