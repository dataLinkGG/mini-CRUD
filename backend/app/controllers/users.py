from flask import request, jsonify
from . import api
from app.models.users import UserCreate
from app.services.users import Users

from flask_jwt_extended import create_access_token
from app.services.users import authenticate_user


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


@api.post("/login")
def login_user():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return {"msg": "Missing username or password"}, 400

    user = authenticate_user(username, password)

    if user:
        access_token = create_access_token(identity=user["id"])

        return {"access_token": access_token}, 200
    else:
        return {"msg": "Invalid credentials"}, 401
