from flask import request, jsonify
from . import api
from app.models.task import TaskCreate
from app.services.task import Tasks


@api.post("/task")
def create_task():
    data = request.get_json(force=True, silent=False)
    payload = TaskCreate(**data)
    task = Tasks.create(payload)
    return jsonify(task.model_dump()), 201


@api.get("/tasks")
def list_tasks():
    tasks = Tasks.get_many()
    return jsonify([t.model_dump() for t in tasks]), 200
