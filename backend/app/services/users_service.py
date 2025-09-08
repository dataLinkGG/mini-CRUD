from typing import List
from app.models.schemas import UserCreate, UserOut
from app.repositories import users_repository as repo


def create_user(payload: UserCreate) -> UserOut:
    uid, email, name = repo.create_user(payload.email, payload.name)
    return UserOut(id=uid, email=email, name=name)


def list_users() -> List[UserOut]:
    rows = repo.list_users()
    return [UserOut.model_validate(row) for row in rows]
