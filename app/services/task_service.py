import uuid
from app.storage.repository import tasks_db

class TaskService:
    def create_task(self, task):
        task_id = str(uuid.uuid4())
        tasks_db[task_id] = {
            "id": task_id,
            "title": task.title,
            "description": task.description,
            "status": "PENDING"
        }
        return tasks_db[task_id]

    def get_all_tasks(self):
        return list(tasks_db.values())

    def get_task(self, task_id):
        return tasks_db.get(task_id)

    def update_task(self, task_id, data):
        task = tasks_db.get(task_id)
        if not task:
            return None
        update_data = data.model_dump(exclude_unset=True)
        task.update(update_data)
        return task

    def delete_task(self, task_id):
        return tasks_db.pop(task_id, None)

task_service = TaskService()
