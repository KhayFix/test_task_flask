from flask import Flask

from webapp.config import Configuration
from webapp.service_app.views import blueprint as service_app_blueprint


def create_app():
    app = Flask(__name__)
    app.config.from_object(Configuration)
    # подключаем блюпринт
    app.register_blueprint(service_app_blueprint)
    return app
