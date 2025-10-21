from flask import request, jsonify

from app.repositories.users import get_user
from . import api
from app.models.users import UserCreate
from app.services.users import Users

from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from app.services.users import authenticate_user


@api.post("/users")
def create_user():
    data = request.get_json(force=True, silent=False)
    payload = UserCreate(**data)
    user = Users.create(payload)
    return jsonify(user.model_dump()), 201


@api.get("/me")
@jwt_required()
def get_current_user():
    current_user_id = get_jwt_identity()
    user = get_user(current_user_id)
    return jsonify(user.model_dump()), 200


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
