from lib.hash import hash_password
from lib import db
from .models import User, Connection


# USER TABLE
def check_is_email_exist(email):
    user = User.query.filter_by(email=email).first()
    return user if user else None


def create_new_user(username, email, password, code):
    new_user = User(username, email, hash_password(password), code)
    db.session.add(new_user)
    db.session.commit()
    return new_user


def get_user_by_sid(sid):
    connection = Connection.query.filter_by(sid=sid).first()
    if connection:
        user = User.query.filter_by(id=connection.user_id).first()
        if user:
            return user
    return None


# CONNECTION
def create_new_connection(sid, token, user_id, data):
    new_connection = Connection(sid, token, user_id, data)
    db.session.add(new_connection)
    db.session.commit()
    return new_connection


def get_connection_by_token_if_exist_connect(token, new_sid):
    connection = Connection.query.filter_by(token=token).first()
    if connection:
        connection.sid = new_sid
        db.session.commit()
        return connection
    return None


def delete_connection_by_token(token):
    connection = Connection.query.filter_by(token=token).first()
    if connection:
        db.session.delete(connection)
        db.session.commit()
        return True
    return False
