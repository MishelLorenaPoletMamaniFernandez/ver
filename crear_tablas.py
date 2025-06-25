from app import db
from models.modelos import Usuario  # importa todos tus modelos aquí

db.create_all()
print("¡Tablas creadas correctamente!")
