from flask import request, jsonify
from . import api
from app.models.users import UserCreate
from app.services.users import Users


@api.post("/users")
def create_user():
    data = request.get_json(force=True, silent=False)
    payload = UserCreate(**data)
    user = Users.create(payload)
    return jsonify(user.model_dump()), 201


@api.get("/users")
def list_users():
    users = Users.get_many()
    return jsonify([u.model_dump() for u in users]), 200
