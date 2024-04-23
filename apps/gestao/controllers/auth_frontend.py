from flask import Blueprint, render_template

auth_frontend_bp = Blueprint('auth_frontend', __name__)

@auth_frontend_bp.route('/login', methods=['GET'])
def login():
    return render_template('authentication/login.html')

@auth_frontend_bp.route('/logout', methods=['GET'])
def logout():
    return render_template('home.html')
