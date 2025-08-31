from flask import request, jsonify
from . import api
from app.models.schemas import UserCreate
from app.services import users_service


@api.post("/users")
def create_user():
    data = request.get_json(force=True, silent=False)
    payload = UserCreate(**data)
    user = users_service.create_user(payload)
    return jsonify(user.model_dump()), 201


@api.get("/users")
def list_users():
    users = users_service.list_users()
    return jsonify([u.model_dump() for u in users]), 200
