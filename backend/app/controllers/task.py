from flask import request, jsonify
from flask_jwt_extended import jwt_required
from . import api
from app.models.task import TaskCreate, TaskUpdate
from app.services.task import Tasks


@api.post("/task")
@jwt_required()
def create_task():
    data = request.get_json(force=True, silent=False)
    payload = TaskCreate(**data)
    task = Tasks.create(payload)
    return jsonify(task.model_dump()), 201


@api.get("/tasks")
@jwt_required()
def list_tasks():
    tasks = Tasks.get_many()
    return jsonify([t.model_dump() for t in tasks]), 200


@api.patch("/task/<int:task_id>")
@jwt_required()
def update_task(task_id: int):
    data = request.get_json(force=True, silent=False)
    payload = TaskUpdate(**data)
    try:
        task = Tasks.update_name(task_id, payload.name)
        return jsonify(task.model_dump()), 200
    except ValueError:
        return jsonify({"error": f"Task id {task_id} not found"}), 404


@api.delete("/task/<int:task_id>")
@jwt_required()
def delete_task(task_id: int):
    deleted = Tasks.delete(task_id)
    if not deleted:
        return jsonify({"error": f"Task id {task_id} not found"}), 404
    return jsonify({"message": f"Task id {task_id} deleted"}), 200
