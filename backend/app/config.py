import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv(override=False)


@dataclass
class Config:
    env: str = os.getenv("FLASK_ENV", "production")
    log_level: str = os.getenv("LOG_LEVEL", "INFO")
    log_dir: str = os.getenv("LOG_DIR", "/logs")

    db_host: str = os.getenv("POSTGRES_HOST", "db")
    db_port: int = int(os.getenv("POSTGRES_PORT", 5432))
    db_name: str = os.getenv("POSTGRES_DB", "appdb")
    db_user: str = os.getenv("POSTGRES_USER", "appuser")
    db_password: str = os.getenv("POSTGRES_PASSWORD", "apppassword")

    @property
    def db_dsn(self) -> str:
        return (
            f"host={self.db_host} port={self.db_port} dbname={self.db_name} "
            f"user={self.db_user} password={self.db_password}"
        )
