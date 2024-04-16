from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required

example_bp = Blueprint('example', __name__, url_prefix='/example')

@example_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    return jsonify({'message': 'This is a protected route'}), 200
