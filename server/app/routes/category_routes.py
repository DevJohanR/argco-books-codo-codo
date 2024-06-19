from flask import Blueprint
from app.controllers.category_controller import create_category, list_categories, get_category

category_bp = Blueprint('category_bp', __name__)

@category_bp.route('/create', methods=['POST'])
def create_category_route():
    return create_category()

@category_bp.route('/', methods=['GET'])
def list_categories_route():
    return list_categories()

@category_bp.route('/<int:category_id>', methods=['GET'])
def get_category_route(category_id):
    return get_category(category_id)
