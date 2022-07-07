import peewee
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

from .repository import *

from flask_jwt_extended import create_access_token

auth = Blueprint('auth', __name__)


@auth.route("/login", methods=["POST"])
def login():
    user_login = request.json.get('login', None)
    password = request.json.get('password', None)
    user = User()
    try:
        user = login_user(user_login, password)
    except user.DoesNotExist:
        return jsonify(error='Пользователя с таким логином не найден')
    except PasswordError:
        return jsonify(error='Неверный пароль')
    access_token = create_access_token(identity=user.login)
    return jsonify(token=access_token,
                   id=user.id,
                   login=user.login)


@auth.route('/register', methods=['POST'])
def register():
    user_login = request.json.get('login', None)
    password = request.json.get('password', None)
    try:
        user = register_user(user_login, password)
    except peewee.IntegrityError:
        return jsonify(error='Пользователь с таким логином уже существует')
    access_token = create_access_token(identity=user.login)
    return jsonify(token=access_token,
                   id=user.id,
                   login=user.login)


@auth.route('/create_car', methods=['GET'])
@jwt_required()
def create_car():
    car_create()
    return jsonify(status='ok')
