from app.extensions import db
from app.models.book import Book
from app.models.book import Comment
from app.models.book import Rating
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
    books_list = [
        {
            'id': book.id,
            'title': book.title,
            'cover': book.cover,
            'synopsis': book.synopsis,
            'publish_date': book.publish_date,
            'author': {'id': book.author.id, 'name': book.author.name},
            'category': {'id': book.category.id, 'name': book.category.name}
        }
        for book in books
    ]
    
    return jsonify({'status': 'success', 'books': books_list})

def get_book(book_id):
    book = Book.query.get_or_404(book_id)
    return jsonify({'id': book.id, 'title': book.title})

def add_comment(book_id):
    book = Book.query.get(book_id)
    if not book:
        return jsonify({'error': 'Book not found'}), 404

    data = request.get_json()
    comment = Comment(content=data['content'], book_id=book_id)
    db.session.add(comment)
    db.session.commit()
    return jsonify({'id': comment.id, 'content': comment.content}), 201
    book = Book.query.get(book_id)
    if not book:
        return jsonify({'error': 'Book not found'}), 404

    data = request.get_json()
    comment = Comment(content=data['content'], book_id=book_id)
    db.session.add(comment)
    db.session.commit()
    return jsonify({'id': comment.id, 'content': comment.content}), 201

def add_rating(book_id):
    book = Book.query.get(book_id)
    if not book:
        return jsonify({'error': 'Book not found'}), 404

    data = request.get_json()
    rating = Rating(score=data['score'], book_id=book_id)
    db.session.add(rating)
    db.session.commit()
    return jsonify({'id': rating.id, 'score': rating.score}), 201
    data = request.get_json()
    book = Book.query.get(book_id)
    if not book:
        return jsonify({'error': 'Book not found'}), 404

    rating = Rating(score=data['score'], user_id=data['user_id'], book_id=book_id)
    db.session.add(rating)
    db.session.commit()
    return jsonify(rating.serialize()), 201


def list_comments(book_id):
    book = Book.query.get(book_id)
    if not book:
        return jsonify({'error': 'Book not found'}), 404

    comments = Comment.query.filter_by(book_id=book_id).all()
    return jsonify([{'id': comment.id, 'content': comment.content, 'created_at': comment.created_at} for comment in comments])


def list_ratings(book_id):
    book = Book.query.get(book_id)
    if not book:
        return jsonify({'error': 'Book not found'}), 404

    ratings = Rating.query.filter_by(book_id=book_id).all()
    return jsonify([{'id': rating.id, 'score': rating.score, 'created_at': rating.created_at} for rating in ratings])



def update_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        return jsonify({'error': 'Book not found'}), 404

    data = request.get_json()
    try:
        if 'title' in data:
            book.title = data['title']
        if 'synopsis' in data:
            book.synopsis = data['synopsis']
        # Agrega aquí más campos si necesitas actualizar otros atributos

        db.session.commit()
        return jsonify({'success': 'Book updated successfully', 'book': {
            'id': book.id,
            'title': book.title,
            'synopsis': book.synopsis
            # Añade aquí más campos si actualizaste otros atributos
        }}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to update book', 'message': str(e)}), 500

def delete_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        return jsonify({'error': 'Book not found'}), 404

    try:
        db.session.delete(book)
        db.session.commit()
        return jsonify({'success': 'Book deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to delete book', 'message': str(e)}), 500