import json
import datetime
from flask import Flask
from apis.blog_api import blog_bp
from apis.home_api import home_bp
from apis.database_crud_api import dp_bp








def create_app():
    
    app = Flask(__name__)

    # Register Blueprints
    app.register_blueprint(home_bp)  # 
    app.register_blueprint(blog_bp, url_prefix='/mongo')
    app.register_blueprint(dp_bp, url_prefix='/mongo/crud')

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(port = 5000 , debug=True)

