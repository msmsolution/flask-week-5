from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)

from app import routes, models



def create_app(config_class=Config):
    app = Flask(__name__)
    from app.api_blueprint import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')