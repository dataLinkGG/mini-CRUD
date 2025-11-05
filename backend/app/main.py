from flask import Flask, jsonify
from flask.json.provider import DefaultJSONProvider
from flask_jwt_extended import JWTManager
from app.config import Config
from app.utils.logger import setup_logging
from app.utils.errors import register_error_handlers
from app.repositories.database import init_pool
from app.controllers import api
from app.controllers import health, users, task  # noqa: F401 (ensures routes load)
from pydantic import BaseModel
from datetime import datetime


class CustomJSONProvider(DefaultJSONProvider):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        if isinstance(obj, BaseModel):
            return obj.model_dump()
        return super().default(obj)


app = Flask(__name__)
config = Config()
app.config.from_mapping(config.__dict__)
app.json = CustomJSONProvider(app)

setup_logging(config.log_dir, config.log_level)

init_pool(config.db_dsn)

app.register_blueprint(api, url_prefix="/api")

register_error_handlers(app)

jwt = JWTManager(app)


@jwt.unauthorized_loader
def unauthorized_callback(err):
    return jsonify({"msg": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def invalid_token_callback(err):
    return jsonify({"msg": f"Invalid token: {err}"}), 422


@app.get("/")
def root():
    return {"service": "flask-no-orm", "env": config.env}
