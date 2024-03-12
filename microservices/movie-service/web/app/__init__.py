from typing import Any, Mapping, Optional

from flask import Flask
from flask_cors import CORS


def create_app(test_config: Optional[Mapping[str, Any]] = None) -> Flask:
    app = Flask(__name__)
    CORS(app)
    app.config.from_object("config")

    if test_config is not None:
        app.config.from_mapping(test_config)
    from app.common.util.db import db

    try:
        db.init_app(app)
    except Exception as e:
        app.logger.critical(str(e))


    from app.modules.movie import movie_controller


    app.register_blueprint(movie_controller.bp)


    return app
