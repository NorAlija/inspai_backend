import os
import secrets
from flask import Flask
from dotenv import load_dotenv
from flask_cors import CORS


#The Application Factory
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)

    app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
    app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
    app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
    app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')
    app.config['SECRET_KEY'] = secrets.token_hex(32)
    
    
    if test_config is None:
        #load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        #load the test config if passed in
        app.config.from_mapping(test_config)
    
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    from . import db
    db.init_app(app)
    
    from . import auth
    app.register_blueprint(auth.bp)
    
    return app


