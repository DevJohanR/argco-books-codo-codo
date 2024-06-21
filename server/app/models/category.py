from app.extensions import db

class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    categorized_books = db.relationship('Book', backref='category', lazy=True)

    def __init__(self, name):
        self.name = name
