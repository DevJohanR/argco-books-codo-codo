from flask import Blueprint, jsonify, request
from app.models.book import Book
from app.extensions import db
from app.models.book import Book
from app.models.author import Author
from app.models.category import Category


main_bp = Blueprint('main', __name__)

main_bp.route('/test-db')
def test_db():
    try:
        book_count = Book.query.count()
        return jsonify({'status': 'success', 'book_count': book_count})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

