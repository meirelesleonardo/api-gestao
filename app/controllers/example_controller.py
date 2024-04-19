from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
import os

example_bp = Blueprint('example', __name__, url_prefix='/example')

@example_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    return jsonify({'message': 'This is a protected route'}), 200

@example_bp.route('/check-flask-env')
def check_flask_env():
    flask_env = os.environ.get('FLASK_ENV')
    debug = os.environ.get('DEBUG')
    return jsonify({'FLASK_ENV': flask_env, 'DEBUG':debug})