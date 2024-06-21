from flask import Blueprint
from app.controllers.book_controller import create_book, list_books, get_book, update_book, delete_book, add_comment, add_rating, list_comments, list_ratings

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

@book_bp.route('/<int:book_id>', methods=['PUT'])
def update_book_route(book_id):
    return update_book(book_id)

@book_bp.route('/<int:book_id>', methods=['DELETE'])
def delete_book_route(book_id):
    return delete_book(book_id)

@book_bp.route('/<int:book_id>/comments', methods=['POST'])
def add_comment_route(book_id):
    return add_comment(book_id)

@book_bp.route('/<int:book_id>/comments', methods=['GET'])
def list_comments_route(book_id):
    return list_comments(book_id)

@book_bp.route('/<int:book_id>/ratings', methods=['POST'])
def add_rating_route(book_id):
    return add_rating(book_id)

@book_bp.route('/<int:book_id>/ratings', methods=['GET'])
def list_ratings_route(book_id):
    return list_ratings(book_id)
