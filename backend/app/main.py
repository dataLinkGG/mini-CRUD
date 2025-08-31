from flask import Flask
from app.config import Config
from app.utils.logger import setup_logging
from app.utils.errors import register_error_handlers
from app.repositories.db import init_pool
from app.routes import api
from app.routes import health, users  # noqa: F401 (ensures routes load)

config = Config()

app = Flask(__name__)

# Logging
setup_logging(config.log_dir, config.log_level)

# DB pool
init_pool(config.db_dsn)

# Blueprints
app.register_blueprint(api, url_prefix="/api")

# Errors
register_error_handlers(app)


# Optional root route
@app.get("/")
def root():
    return {"service": "flask-no-orm", "env": config.env}
