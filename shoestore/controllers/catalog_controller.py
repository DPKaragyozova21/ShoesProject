from flask import Blueprint, render_template, request
from services.catalog_service import catalog_service

catalog_bp = Blueprint('catalog_bp', __name__)


@catalog_bp.route('/')
def catalog():
    search = request.args.get('search', '')
    color = request.args.get('color', '')
    min_price = request.args.get('min_price', type=float)
    max_price = request.args.get('max_price', type=float)
    size = request.args.get('size', '')
    category_id = request.args.get('category', type=int)


    products = catalog_service.search_products(
        search=search,
        color=color,
        min_price=min_price,
        max_price=max_price,
        size=size,
        category_id=category_id
    )

    categories = catalog_service.get_all_categories()
    colors = catalog_service.get_all_colors()
    sizes = catalog_service.get_all_sizes()

    return render_template('catalog.html',
                           products=products,
                           categories=categories,
                           colors=colors,
                           sizes=sizes,
                           search=search,
                           color=color,
                           min_price=min_price,
                           max_price=max_price,
                           size=size,
                           selected_category=category_id)


@catalog_bp.route('/category/<int:category_id>')
def category(category_id):
    category = catalog_service.get_category_by_id(category_id)
    products = catalog_service.search_products(category_id=category_id)
    categories = catalog_service.get_all_categories()
    colors = catalog_service.get_all_colors()
    sizes = catalog_service.get_all_sizes()

    return render_template('catalog.html',
                           products=products,
                           categories=categories,
                           colors=colors,
                           sizes=sizes,
                           selected_category=category_id,
                           category_name=category['name'] if category else None)