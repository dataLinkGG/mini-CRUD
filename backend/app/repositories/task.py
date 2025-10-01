from typing import List, Optional, Tuple
from psycopg2.extras import RealDictCursor
from .database import get_conn, put_conn

SQL_INSERT_TASK = """
INSERT INTO tasks (name, value, scheduled_to, executed_at)
VALUES (%s, %s, %s, %s)
RETURNING id, name, value, created_at, scheduled_to, executed_at;
"""

SQL_LIST_TASKS = """
SELECT id, name, value, created_at, scheduled_to, executed_at
FROM tasks ORDER BY id ASC;
"""

SQL_GET_TASK = """
SELECT id, name, value, created_at, scheduled_to, executed_at
FROM tasks WHERE id = %s;
"""


def create_task(name: str, value: Optional[float], scheduled_to, executed_at) -> dict:
    conn = get_conn()
    try:
        with conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(SQL_INSERT_TASK, (name, value, scheduled_to, executed_at))
                return cur.fetchone()
    finally:
        put_conn(conn)


def list_tasks() -> List[dict]:
    conn = get_conn()
    try:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(SQL_LIST_TASKS)
            return cur.fetchall()
    finally:
        put_conn(conn)


def get_task(task_id: int) -> Optional[dict]:
    conn = get_conn()
    try:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(SQL_GET_TASK, (task_id,))
            return cur.fetchone()
    finally:
        put_conn(conn)
