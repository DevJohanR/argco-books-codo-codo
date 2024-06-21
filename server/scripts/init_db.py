# scripts/init_db.py
import os
import sys
from dotenv import load_dotenv

# Agregar el directorio principal del proyecto al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.main import create_app
from app.extensions import db

# Cargar variables de entorno desde el archivo .env
load_dotenv()

app = create_app()

with app.app_context():
    db.create_all()
    print("Base de datos inicializada.")
