import json
import datetime
from flask import Flask
from apis.blog_api import blog_bp
from apis.home_api import home_bp
from apis.database_crud_api import dp_bp
import os
import logging
from werkzeug.middleware.proxy_fix import ProxyFix


def create_app():
    app = Flask(__name__)

    # Load config from environment or fallback
    #app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev_default_secret')
    app.config['DEBUG'] = os.environ.get('FLASK_DEBUG', 'False') == 'True'

    # Register Blueprints
    app.register_blueprint(home_bp)
    app.register_blueprint(blog_bp, url_prefix='/mongo')
    # app.register_blueprint(dp_bp, url_prefix='/mongo/crud')

    # Apply proxy fix if behind reverse proxy (like NGINX)
    app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1)

    # Set up logging
    if not app.debug:
        handler = logging.StreamHandler()
        handler.setLevel(logging.INFO)
        app.logger.addHandler(handler)

    return app


# Only for development!
if __name__ == '__main__':
    app = create_app()
    app.run(port=5000, debug=True)
