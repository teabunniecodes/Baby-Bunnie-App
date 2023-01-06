from flask import Flask
from flask_login import LoginManager
import sqlite3

# db = sqlite3()
# DB_NAME = "baby_data.db"

def create_app():
    app = Flask (__name__)
    app.config['SECRET_KEY'] = "helloworld"
    
    from .views import views
    from .button_data import buttons
    from .models import User

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(buttons, url_prefix="/")

    login_manager = LoginManager()
    login_manager.login_view = "views.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.retrieve_id(user_id)

    return app

