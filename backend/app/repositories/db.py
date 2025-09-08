import psycopg2
from psycopg2.pool import SimpleConnectionPool
from typing import Optional

_pool: Optional[SimpleConnectionPool] = None


def init_pool(dsn: str):
    global _pool
    if _pool is None:
        _pool = SimpleConnectionPool(minconn=1, maxconn=10, dsn=dsn)
    return _pool


def get_conn():
    if _pool is None:
        raise RuntimeError("DB pool not initialized")
    return _pool.getconn()


def put_conn(conn):
    if _pool is None:
        raise RuntimeError("DB pool not initialized")
    _pool.putconn(conn)
