from app.extensions import db
from app.models.author import Author
from flask import request, jsonify

def get_all_authors():
    authors = Author.query.all()
    authors_data = [author.to_dict() for author in authors]

    return jsonify(authors_data), 200

def get_author_by_id(id):
    author = Author.query.get_or_404(id)

    return jsonify(author.to_dict()), 200
