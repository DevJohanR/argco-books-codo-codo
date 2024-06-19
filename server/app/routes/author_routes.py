from flask import Blueprint
from app.controllers.author_controller import create_author, list_authors, get_author

author_bp = Blueprint('author_bp', __name__)

@author_bp.route('/create', methods=['POST'])
def create_author_route():
    return create_author()

@author_bp.route('/', methods=['GET'])
def list_authors_route():
    return list_authors()

@author_bp.route('/<int:author_id>', methods=['GET'])
def get_author_route(author_id):
    return get_author(author_id)
