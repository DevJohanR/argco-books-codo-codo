from flask import Blueprint
from app.controllers.book_controller import get_all_books, get_book_by_id, create_book, update_book, delete_book

book_bp = Blueprint('book_bp', __name__)

@book_bp.route('/', methods=['GET'])
def get_all():
    return get_all_books()

@book_bp.route('/<int:id>', methods=['GET'])
def get_by_id(id):
    return get_book_by_id(id)

@book_bp.route('/', methods=['POST'])
def create():
    return create_book()

@book_bp.route('/<int:id>', methods=['PUT'])
def update(id):
    return update_book(id)

@book_bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    return delete_book(id)
