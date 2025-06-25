# crear_db_manual.py
from app import create_app, db
from app.models import modelos, producto, usuario

app = create_app()

with app.app_context():
    db.create_all()
    print("✔ Base de datos y tablas creadas correctamente.")
