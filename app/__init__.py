from flask import Flask
import os


def create_app():
    app = Flask(__name__)

    app.secret_key = os.environ.get("FLASK_SECRET_KEY", "dev-key")

    from app.routes import chat_bp
    app.register_blueprint(chat_bp)

    return app
