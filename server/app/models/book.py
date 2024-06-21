from app.extensions import db
from datetime import datetime

class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    isdb = db.Column(db.String(50), nullable=False)
    title = db.Column(db.String(100), unique=True, nullable=False)
    cover = db.Column(db.String(50))
    synopsis = db.Column(db.String(400), nullable=False)
    publish_date = db.Column(db.DateTime)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    comments = db.relationship('Comment', backref='book', lazy='dynamic')
    ratings = db.relationship('Rating', backref='book', lazy='dynamic')

    def __init__(self, isdb, title, cover, synopsis, publish_date, author_id, category_id):
        self.isdb = isdb
        self.title = title
        self.cover = cover
        self.synopsis = synopsis
        self.publish_date = publish_date
        self.author_id = author_id
        self.category_id = category_id


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, content, book_id):
        self.content = content
        self.book_id = book_id

class Rating(db.Model):
    __tablename__ = 'ratings'
    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Float, nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, score, book_id):
        self.score = score
        self.book_id = book_id