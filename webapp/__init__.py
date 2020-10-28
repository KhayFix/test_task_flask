from flask import Flask

from webapp.config import Configuration
from webapp.db import db
from webapp.service_app.views import blueprint as service_app_blueprint


def create_app():
    app = Flask(__name__)
    app.config.from_object(Configuration)
    db.init_app(app)
    # подключаем блюпринт
    app.register_blueprint(service_app_blueprint)
    return app
