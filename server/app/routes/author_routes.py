from flask import Blueprint
from app.controllers.author_controller import get_all_authors, get_author_by_id

author_bp = Blueprint('author_bp', __name__)

@author_bp.route('/', methods=['GET'])
def get_all():
    return get_all_authors()

@author_bp.route('/<int:id>', methods=['GET'])
def get_by_id(id):
    return get_author_by_id(id)
