from typing import List, Optional, Tuple
from .database import get_conn, put_conn

SQL_INSERT_USER = """
INSERT INTO users (email, name) VALUES (%s, %s)
RETURNING id, email, name;
"""

SQL_LIST_USERS = """
SELECT id, email, name FROM users ORDER BY id ASC;
"""

SQL_GET_USER = """
SELECT id, email, name FROM users WHERE id = %s;
"""


def create_user(email: str, name: str) -> Tuple[int, str, str]:
    conn = get_conn()
    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute(SQL_INSERT_USER, (email, name))
                row = cur.fetchone()
                return row  # (id, email, name)
    finally:
        put_conn(conn)


def list_users() -> List[Tuple[int, str, str]]:
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute(SQL_LIST_USERS)
            return cur.fetchall()
    finally:
        put_conn(conn)


def get_user(user_id: int) -> Optional[Tuple[int, str, str]]:
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute(SQL_GET_USER, (user_id,))
            return cur.fetchone()
    finally:
        put_conn(conn)
