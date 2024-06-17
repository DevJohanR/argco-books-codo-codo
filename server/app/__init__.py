from flask import Flask
from .config import Config
from .extensions import db
from .models import book, author, category
from .routes.main import main_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Inicializar extensiones
    db.init_app(app)
    
    # Registrar Blueprints
    app.register_blueprint(main_bp)

    return app