import json
import logging
from flask import jsonify


class JsonRequestFormatter(logging.Formatter):
    def format(self, record):
        base = {
            "level": record.levelname,
            "message": record.getMessage(),
            "logger": record.name,
        }
        if record.exc_info:
            base["exc_info"] = self.formatException(record.exc_info)
        return json.dumps(base, ensure_ascii=False)


def register_error_handlers(app):
    @app.errorhandler(400)
    def bad_request(e):
        return jsonify(error="bad_request", message=str(e)), 400

    @app.errorhandler(404)
    def not_found(e):
        return jsonify(error="not_found"), 404

    @app.errorhandler(500)
    def server_error(e):
        app.logger.exception("Unhandled error")
        return jsonify(error="server_error"), 500
