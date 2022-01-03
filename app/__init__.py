from flask import Flask
from flask_login import LoginManager


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '921f65242c8ef3e3db332717392fb2cfb830ecc0bf124f7368a9ddbf415ac007'

    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        from app.persistance.model import User
        return User.find(email=user_id).first_or_none()

    from app.blueprints.open import bp_open
    app.register_blueprint(bp_open)

    from app.blueprints.user import bp_user
    app.register_blueprint(bp_user, url_prefix='/user')

    from app.blueprints.admin import bp_admin
    app.register_blueprint(bp_admin, url_prefix='/admin')
    return app


if __name__ == '__main__':
    create_app().run()
