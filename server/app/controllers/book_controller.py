from app.extensions import db
from app.models.book import Book
from app.models.author import Author
from app.models.category import Category
from flask import request, jsonify
from datetime import datetime

def create_book():
    data = request.get_json()

    # Verificar si el autor existe
    author = Author.query.get(data['author_id'])
    if not author:
        return jsonify({'error': 'Author not found'}), 404

    # Verificar si la categoría existe
    category = Category.query.get(data['category_id'])
    if not category:
        return jsonify({'error': 'Category not found'}), 404

    publish_date = datetime.strptime(data['publish_date'], '%Y-%m-%d')
    new_book = Book(
        isdb=data['isdb'], 
        title=data['title'], 
        cover=data['cover'],
        synopsis=data['synopsis'], 
        publish_date=publish_date,
        author_id=data['author_id'],
        category_id=data['category_id']
    )
    db.session.add(new_book)
    db.session.commit()
    return jsonify({'id': new_book.id, 'title': new_book.title}), 201

def list_books():
    books = Book.query.all()
    return jsonify([{'id': book.id, 'title': book.title, 'author_id': book.author_id, 'category_id': book.category_id} for book in books])

def get_book(book_id):
    book = Book.query.get_or_404(book_id)
    return jsonify({'id': book.id, 'title': book.title})
