from typing import List
from app.models.task import TaskCreate, TaskRead
from app.repositories.task import create_task, list_tasks, update_task_name


class Tasks:
    @staticmethod
    def create(payload: TaskCreate) -> TaskRead:
        row = create_task(
            payload.name,
            payload.value,
            payload.scheduled_to,
            payload.executed_at,
        )
        return TaskRead.model_validate(row)

    @staticmethod
    def get_many() -> List[TaskRead]:
        rows = list_tasks()
        return [TaskRead.model_validate(row) for row in rows]

    @staticmethod
    def update_name(task_id: int, new_name: str) -> TaskRead:
        row = update_task_name(task_id, new_name)
        if not row:
            raise ValueError("Task not found")
        return TaskRead.model_validate(row)
