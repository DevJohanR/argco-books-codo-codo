from app.extensions import db

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    authored_books = db.relationship('Book', backref='author', lazy=True)

    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name
