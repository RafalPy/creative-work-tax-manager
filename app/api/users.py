from flask import Blueprint, jsonify

users_bp = Blueprint('users', __name__)

@users_bp.route('/', methods=['GET'])
def get_users():
    return jsonify({'users': ['Alice', 'Bob']}) #tutaj zwracanie z bazy wstawić

@users_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    return jsonify({'user_id': user_id})