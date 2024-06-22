from flask import Blueprint
from app.controllers.category_controller import get_all_categories, get_category_by_id

category_bp = Blueprint('category_bp', __name__)

@category_bp.route('/', methods=['GET'])
def get_all():
    return get_all_categories()

@category_bp.route('/<int:id>', methods=['GET'])
def get_by_id(id):
    return get_category_by_id(id)
