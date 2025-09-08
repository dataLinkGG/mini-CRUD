from typing import List
from app.models.schemas import UserCreate, UserRead
from app.repositories import users_repository as repo


def create_user(payload: UserCreate) -> UserRead:
    uid, email, name = repo.create_user(payload.email, payload.name)
    return UserRead(id=uid, email=email, name=name)


def list_users() -> List[UserRead]:
    rows = repo.list_users()
    return [UserRead.model_validate(row) for row in rows]
