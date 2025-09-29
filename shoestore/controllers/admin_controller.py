
from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from services.catalog_service import catalog_service

admin_bp = Blueprint('admin_bp', __name__)


def admin_required():
    if 'user_email' not in session or not session.get('is_admin'):
        return redirect(url_for('auth_bp.login'))
    return None


@admin_bp.route('/')
def admin_panel():
    redirect_response = admin_required()
    if redirect_response:
        return redirect_response

    products = catalog_service.get_all_products()
    return render_template('admin/panel.html', products=products)


@admin_bp.route('/add_product', methods=['GET', 'POST'])
def add_product():
    redirect_response = admin_required()
    if redirect_response:
        return redirect_response

    if request.method == 'POST':
        product_data = {
            'name': request.form['name'],
            'description': request.form['description'],
            'color': request.form['color'],
            'price': float(request.form['price']),
            'stock': int(request.form['stock']),
            'image_url': request.form['image_url'],
            'sizes': request.form['sizes'].split(',')
        }

        catalog_service.add_product(product_data)
        flash('Product added successfully!', 'success')
        return redirect(url_for('admin_bp.admin_panel'))

    return render_template('admin/add_product.html')


@admin_bp.route('/edit_product/<int:product_id>', methods=['GET', 'POST'])
def edit_product(product_id):
    redirect_response = admin_required()
    if redirect_response:
        return redirect_response

    product = catalog_service.get_product_by_id(product_id)

    if request.method == 'POST':
        product_data = {
            'name': request.form['name'],
            'description': request.form['description'],
            'color': request.form['color'],
            'price': float(request.form['price']),
            'stock': int(request.form['stock']),
            'image_url': request.form['image_url'],
            'sizes': request.form['sizes'].split(',')
        }

        catalog_service.update_product(product_id, product_data)
        flash('Product updated successfully!', 'success')
        return redirect(url_for('admin_bp.admin_panel'))

    return render_template('admin/edit_product.html', product=product)


@admin_bp.route('/delete_product/<int:product_id>')
def delete_product(product_id):
    redirect_response = admin_required()
    if redirect_response:
        return redirect_response

    catalog_service.delete_product(product_id)
    flash('Product deleted successfully!', 'success')
    return redirect(url_for('admin_bp.admin_panel'))