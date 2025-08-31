import logging
import os
from logging.handlers import RotatingFileHandler
from .errors import JsonRequestFormatter


def setup_logging(log_dir: str, level: str = "INFO"):
    os.makedirs(log_dir, exist_ok=True)

    logger = logging.getLogger()
    logger.setLevel(level.upper())

    # Console handler
    ch = logging.StreamHandler()
    ch.setFormatter(JsonRequestFormatter())
    logger.addHandler(ch)

    # Rotating file handler
    fh = RotatingFileHandler(
        filename=os.path.join(log_dir, "app.log"),
        maxBytes=2 * 1024 * 1024,  # 2MB
        backupCount=5,
    )
    fh.setFormatter(JsonRequestFormatter())
    logger.addHandler(fh)

    logging.getLogger("gunicorn.error").setLevel(level.upper())
    logging.getLogger("gunicorn.access").setLevel(level.upper())

    return logger
