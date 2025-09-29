
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

    products = catalog_service.search_products(search, color, min_price, max_price, size)
    colors = catalog_service.get_all_colors()
    sizes = catalog_service.get_all_sizes()

    return render_template('catalog.html',
                           products=products,
                           colors=colors,
                           sizes=sizes,
                           search=search,
                           color=color,
                           min_price=min_price,
                           max_price=max_price,
                           size=size)