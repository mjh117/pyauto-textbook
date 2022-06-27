import os
from flask import Flask

def create_app():
    app = Flask(__name__)

    from .views import ex, bk
    app.register_blueprint(ex)
    app.register_blueprint(bk)
    app.secret_key = 'secret key'

    return app