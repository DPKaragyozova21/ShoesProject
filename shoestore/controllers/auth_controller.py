
from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from services.auth_service import auth_service

auth_bp = Blueprint('auth_bp', __name__)


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        name = request.form['name']

        if auth_service.register_user(email, password, name):
            flash('Registration successful! Please login.', 'success')
            return redirect(url_for('auth_bp.login'))
        else:
            flash('User with this email already exists!', 'error')

    return render_template('register.html')


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = auth_service.login_user(email, password)
        if user:
            session['user_email'] = email
            session['user_name'] = user['name']
            session['is_admin'] = user.get('is_admin', False)
            return redirect(url_for('index'))
        else:
            flash('Invalid email or password!', 'error')

    return render_template('login.html')


@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth_bp.login'))