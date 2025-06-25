# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'clave123'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///masu.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    # Importa modelos
    from app.models import modelos, producto, usuario

    # Registra blueprints
    from app.routes.productos_routes import productos_bp
    app.register_blueprint(productos_bp)

    from app.routes.main_routes import main_bp
    app.register_blueprint(main_bp)

    return app  # 🔴 Esta línea debe tener exactamente 4 espacios

