from typing import List
from app.models.users import UserCreate, UserRead
from app.repositories.users import create_user, get_user_by_username, list_users
from werkzeug.security import generate_password_hash, check_password_hash


class Users:
    @staticmethod
    def create(payload: UserCreate) -> UserRead:
        password_hash = hash_password(payload.password)
        uid, email, name = create_user(payload.email, payload.name, password_hash)

        return UserRead(id=uid, email=email, name=name)

    @staticmethod
    def get_many() -> List[UserRead]:
        rows = list_users()
        return [UserRead.model_validate(row) for row in rows]


def authenticate_user(username: str, password: str) -> dict | None:
    """Finds a user by username and verifies the password."""
    user_data = get_user_by_username(username)

    if user_data and verify_password(user_data["password_hash"], password):
        return user_data

    return None


def hash_password(password: str) -> str:
    """Hashes a password using a strong default method."""
    return generate_password_hash(password)


def verify_password(stored_hash: str, password: str) -> bool:
    """Verifies a password against the stored hash."""
    return check_password_hash(stored_hash, password)
