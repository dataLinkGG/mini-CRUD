from typing import List
from app.models.task import TaskCreate, TaskRead
from app.repositories.task import create_task, list_tasks


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
