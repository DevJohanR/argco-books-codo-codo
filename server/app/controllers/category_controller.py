from app.extensions import db
from app.models.category import Category
from flask import request, jsonify

def create_category():
    data = request.get_json()
    new_category = Category(name=data['name'])
    db.session.add(new_category)
    db.session.commit()
    return jsonify({'id': new_category.id, 'name': new_category.name}), 201

def list_categories():
    categories = Category.query.all()
    return jsonify([{'id': category.id, 'name': category.name} for category in categories])

def get_category(category_id):
    category = Category.query.get_or_404(category_id)
    return jsonify({'id': category.id, 'name': category.name})
