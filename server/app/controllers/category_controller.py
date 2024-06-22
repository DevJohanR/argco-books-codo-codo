from app.extensions import db
from app.models.category import Category
from flask import request, jsonify

def get_all_categories():
    categories = Category.query.all()
    categories_data = [category.to_dict() for category in categories]

    return jsonify(categories_data), 200

def get_category_by_id(id):
    category = Category.query.get_or_404(id)

    return jsonify(category.to_dict()), 200
