from models.Car import Car
from models.User import User
from passlib.hash import sha256_crypt


def register_user(login, password):
    hash_password = _hash_password(password)
    user = User(login=login, password=hash_password)
    user.save()
    return user


class PasswordError(Exception):
    """Error for invalid password"""
    pass


def login_user(login, password):
    user = User.get(User.login == login)
    if sha256_crypt.verify(password, user.password):
        return user
    else:
        raise PasswordError


def _hash_password(password):
    password = sha256_crypt.encrypt(password)
    return password


def car_create():
    user = User.get(User.login == 'login')
    # car1 = Car(name='Car1', model='Car1_model', user=user)
    # car1.save()
    # car2 = Car(name='Car2', model='Car2_model', user=user)
    # car2.save()
    for i in user.car_details:
        print(i.name)
