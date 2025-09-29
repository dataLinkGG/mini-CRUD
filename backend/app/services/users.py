from typing import List
from app.models.users import UserCreate, UserRead
from app.repositories.users import create_user, list_users


def create_user(payload: UserCreate) -> UserRead:
    uid, email, name = create_user(payload.email, payload.name)
    return UserRead(id=uid, email=email, name=name)


def list_users() -> List[UserRead]:
    rows = list_users()
    return [UserRead.model_validate(row) for row in rows]
