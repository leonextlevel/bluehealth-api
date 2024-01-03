import os

from apiflask import APIFlask

from .config import config_by_name
from .database import db


def create_app(config_name: str) -> APIFlask:
    app = APIFlask(__name__)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)

    # Blueprints
    from bluehealth.routes import patients_bp, pharmacies_bp, transactions_bp

    app.register_blueprint(patients_bp)
    app.register_blueprint(pharmacies_bp)
    app.register_blueprint(transactions_bp)

    return app


app = create_app(os.getenv('ENVIRONMENT'))

app.app_context().push()
