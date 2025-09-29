
from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from services.cart_service import cart_service
from services.order_service import order_service

cart_bp = Blueprint('cart_bp', __name__)


@cart_bp.route('/add/<int:product_id>')
def add_to_cart(product_id):
    if 'user_email' not in session:
        return redirect(url_for('auth_bp.login'))

    user_email = session['user_email']
    size = request.args.get('size')

    if cart_service.add_to_cart(user_email, product_id, size):
        flash('Product added to cart!', 'success')
    else:
        flash('Product not available or out of stock!', 'error')

    return redirect(url_for('index'))


@cart_bp.route('/')
def view_cart():
    if 'user_email' not in session:
        return redirect(url_for('auth_bp.login'))

    user_email = session['user_email']
    cart_items = cart_service.get_cart(user_email)
    total = cart_service.get_cart_total(user_email)

    return render_template('cart.html', cart_items=cart_items, total=total)


@cart_bp.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if 'user_email' not in session:
        return redirect(url_for('auth_bp.login'))

    user_email = session['user_email']

    if request.method == 'POST':
        address = request.form['address']
        payment_method = request.form['payment_method']

        if order_service.create_order(user_email, address, payment_method):
            cart_service.clear_cart(user_email)
            flash('Order placed successfully!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Error processing order!', 'error')

    cart_items = cart_service.get_cart(user_email)
    total = cart_service.get_cart_total(user_email)

    return render_template('checkout.html', cart_items=cart_items, total=total)