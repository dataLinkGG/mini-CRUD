from typing import List, Optional, Tuple, Dict, Any
from psycopg2.extras import RealDictCursor
from .database import get_conn, put_conn

# Assuming 'email' is the unique username and 'password_hash' is also in the table
SQL_INSERT_USER = """
INSERT INTO users (email, name, password_hash) VALUES (%s, %s, %s)
RETURNING id, email, name;
"""

SQL_LIST_USERS = """
SELECT id, email, name FROM users ORDER BY id ASC;
"""

SQL_GET_USER = """
SELECT id, email, name FROM users WHERE id = %s;
"""

SQL_GET_USER_BY_EMAIL = """
SELECT id, email, name, password_hash FROM users WHERE email = %s;
"""


def create_user(email: str, name: str, password_hash: str) -> Tuple[int, str, str]:
    """Updated to include password_hash for creation."""
    conn = get_conn()
    try:
        with conn:
            with conn.cursor() as cur:
                # The execute call needs to be updated to accept the password_hash
                cur.execute(SQL_INSERT_USER, (email, name, password_hash))
                row = cur.fetchone()
                return row
    finally:
        put_conn(conn)


def list_users() -> List[Dict[str, Any]]:
    conn = get_conn()
    try:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(SQL_LIST_USERS)
            return cur.fetchall()
    finally:
        put_conn(conn)


def get_user(user_id: int) -> Optional[Dict[str, Any]]:
    conn = get_conn()
    try:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(SQL_GET_USER, (user_id,))
            return cur.fetchone() 
    finally:
        put_conn(conn)


def get_user_by_username(username: str) -> Optional[Dict[str, Any]]:
    """
    Retrieves a user by email (used as username) including the password hash
    for authentication purposes. Returns a dictionary using RealDictCursor.
    """
    conn = get_conn()
    try:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(SQL_GET_USER_BY_EMAIL, (username,))
            return cur.fetchone()
    finally:
        put_conn(conn)
