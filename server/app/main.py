from flask import Flask
from flask_cors import CORS
from app.config import Config
from app.extensions import db
from app.routes.author_routes import author_bp
from app.routes.book_routes import book_bp
from app.routes.category_routes import category_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    CORS(app)  # Habilitar CORS para toda la aplicación
    
    db.init_app(app)
    
    app.register_blueprint(author_bp, url_prefix='/api/authors')
    app.register_blueprint(book_bp, url_prefix='/api/books')
    app.register_blueprint(category_bp, url_prefix='/api/categories')
    
    return app
