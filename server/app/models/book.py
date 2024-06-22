from app.extensions import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(13), nullable=False, unique=True)
    title = db.Column(db.String(255), nullable=False)
    cover = db.Column(db.String(255), nullable=False)
    synopsis = db.Column(db.Text, nullable=False)
    publication_date = db.Column(db.Date, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)

    def __init__(self, isbn, title, cover, synopsis, publication_date, author_id, category_id):
        self.isbn = isbn
        self.title = title
        self.cover = cover
        self.synopsis = synopsis
        self.publication_date = publication_date
        self.author_id = author_id
        self.category_id = category_id

    def to_dict(self): 
        return {
            'id': self.id,
            'isbn': self.isbn,
            'title': self.title,
            'cover': self.cover,
            'synopsis': self.synopsis,
            'publication_date': self.publication_date,
            'author': self.author.to_dict(),
            'category': self.category.to_dict()
        }
