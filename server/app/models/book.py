from ..extensions import db

class Book(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    isdb = db.Column(db.String(50),nulleable=False)
    title = db.Column(db.String(100), unique=True, nulleable=False)
    cover = db.Column(db.String(50))
    synopsis = db.Column(db.String(400), nulleable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))


    def __init__(self,isdb,title,cover,synopsis,author_id,category_id):
        
        self.isdb = isdb
        self.title = title
        self.cover = cover
        self.synopsis = synopsis
        self.author_id = author_id
        self.category_id = category_id