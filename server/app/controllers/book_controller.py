from app.extensions import db
from app.models.book import Book
from app.models.author import Author
from app.models.category import Category
from flask import request, jsonify

def get_all_books():
    books = Book.query.all()
    books_data = [book.to_dict() for book in books]

    return jsonify(books_data), 200

def get_book_by_id(id):
    book = Book.query.get_or_404(id)

    return jsonify(book.to_dict()), 200

def create_book():
    data = request.get_json()

    # Extract data from JSON
    isbn = data['isbn']
    title = data['title']
    cover = data['cover']
    synopsis = data['synopsis']
    publication_date = data['publication_date']
    author = data['author']
    category_id = data['category_id']

    # Check if category_id exists
    category = Category.query.get(category_id)

    if not category:
        return jsonify({'error': 'Category not found'}), 404

    # Check if author exists, create if not
    author_first_name, author_last_name = author.split()
    author = Author.query.filter_by(first_name=author_first_name, last_name=author_last_name).first()

    if not author:
        author = Author(first_name=author_first_name, last_name=author_last_name)
        db.session.add(author)
        db.session.commit()

    # Create book instance
    new_book = Book(
        isbn=isbn,
        title=title,
        cover=cover,
        synopsis=synopsis,
        publication_date=publication_date,
        author_id=author.id,
        category_id=category_id
    )

    # Save book to database
    db.session.add(new_book)
    db.session.commit()

    return jsonify(new_book.to_dict()), 201

def update_book(id):
    book = Book.query.get_or_404(id)
    data = request.get_json()

    # Update book fields
    book.isbn = data['isbn']
    book.title = data['title']
    book.cover = data['cover']
    book.synopsis = data['synopsis']
    book.publication_date = data['publication_date']

    #Check if category_id exists
    category_id = data['category_id']
    category = Category.query.get(category_id)
    
    if not category:
        return jsonify({'error': 'Category not found'}), 404

    # Check and update author if provided
    if 'author' in data:
        author = data['author']
        author_first_name, author_last_name = author.split()
        
        # Check if author exists, create if not
        author = Author.query.filter_by(first_name=author_first_name, last_name=author_last_name).first()
        if not author:
            author = Author(first_name=author_first_name, last_name=author_last_name)
            db.session.add(author)
            db.session.commit()
        
        # Update book's author_id
        book.author_id = author.id

    db.session.commit()

    return jsonify(book.to_dict()), 200

def delete_book(id):
    book = Book.query.get_or_404(id)
    
    db.session.delete(book)
    db.session.commit()
    
    return '', 204
