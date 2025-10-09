from flask import Flask
from flask.json.provider import DefaultJSONProvider
from app.config import Config
from app.utils.logger import setup_logging
from app.utils.errors import register_error_handlers
from app.repositories.database import init_pool
from app.controllers import api
from app.controllers import health, users, task  # noqa: F401 (ensures routes load)
from pydantic import BaseModel
from datetime import datetime

config = Config()


class CustomJSONProvider(DefaultJSONProvider):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        if isinstance(obj, BaseModel):
            return obj.model_dump()
        return super().default(obj)


app = Flask(__name__)
app.json = CustomJSONProvider(app)

setup_logging(config.log_dir, config.log_level)

init_pool(config.db_dsn)

app.register_blueprint(api, url_prefix="/api")

register_error_handlers(app)


@app.get("/")
def root():
    return {"service": "flask-no-orm", "env": config.env}
