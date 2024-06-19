from app.extensions import db
from app.models.author import Author
from flask import request, jsonify

def create_author():
    data = request.get_json()
    new_author = Author(name=data['name'], last_name=data.get('last_name', ''))
    db.session.add(new_author)
    db.session.commit()
    return jsonify({'id': new_author.id, 'name': new_author.name, 'last_name': new_author.last_name}), 201

def list_authors():
    authors = Author.query.all()
    return jsonify([{'id': author.id, 'name': author.name, 'last_name': author.last_name} for author in authors])

def get_author(author_id):
    author = Author.query.get_or_404(author_id)
    return jsonify({'id': author.id, 'name': author.name, 'last_name': author.last_name})
