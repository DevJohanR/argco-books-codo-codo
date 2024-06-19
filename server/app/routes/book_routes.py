from flask import Blueprint
from app.controllers.book_controller import create_book, list_books, get_book

book_bp = Blueprint('book_bp', __name__)

@book_bp.route('/create', methods=['POST'])
def create_book_route():
    return create_book()

@book_bp.route('/', methods=['GET'])
def list_books_route():
    return list_books()

@book_bp.route('/<int:book_id>', methods=['GET'])
def get_book_route(book_id):
    return get_book(book_id)
