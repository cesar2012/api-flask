from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
   
    app = Flask(__name__)

    # Configuración del poyecto 
    app.config.from_object('config.Config')

    db.init_app(app)


    # Registrar Bluprint
    from . import controller
    app.register_blueprint(controller.bp)


    # from . import auth
    # app.register_blueprint(auth.bp)



    with app.app_context():
        db.create_all()

    return app