
from flask import Flask
from flask_cors import CORS
from app.config import Config
from app.extensions import db
from app.models.book import Book
from app.models.author import Author
from app.models.category import Category
from app.routes.main import main_bp



def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Inicializar extensiones
    db.init_app(app)
    CORS(app)
    with app.app_context():
       db.create_all()
            
     

    # Registrar Blueprints
    app.register_blueprint(main_bp)

    return app