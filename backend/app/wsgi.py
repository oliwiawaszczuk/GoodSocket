from datetime import datetime

from flask import request
from app import create_app
from app.query import check_is_email_exist, create_new_user, create_new_connection, get_user_by_sid, \
    get_connection_by_token_if_exist_connect, delete_connection_by_token
from lib.creator import create_user_code, create_token
from lib.hash import verify_password
from lib import db, migrate

app, socketio = create_app(db, migrate)


@socketio.on('connect')
def connect():
    sid = request.sid
    print(f"connected sid: {sid}")


@socketio.on('disconnect')
def disconnect():
    sid = request.sid
    print(f"disconnected sid: {sid}")


@socketio.on('message')
def message(_message):
    sid = request.sid
    print(f"message {_message}, from sid: {sid} and user: {get_user_by_sid(sid)}")


@socketio.on('auto_login')
def auto_login(token):
    sid = request.sid
    if token:
        connection = get_connection_by_token_if_exist_connect(token, sid)
        if connection:
            user = get_user_by_sid(sid)
            socketio.emit('success-login', {'username': user.username, 'userCode': user.code, 'token': connection.token}, to=sid)


@socketio.on('login')
def login(data, sid=None):
    if sid is None:
        sid = request.sid

    email = data.get('email', '').strip()
    password = data.get('password', '').strip()
    if email == '' or password == '':
        socketio.emit('failed-login', 'fields email and password cannot be empty', to=sid)
        return

    user = check_is_email_exist(email)
    if user is None:
        socketio.emit('failed-login', 'user with this email does not exist', to=sid)
        return

    if not verify_password(password, user.password):
        socketio.emit('failed-login', 'wrong password', to=sid)
        return

    token = create_token(8)
    new_connection = create_new_connection(sid, token, user.id, datetime.now())
    socketio.emit('success-login', {'email': email, 'username': user.username, 'userCode': user.code, 'token': token}, to=sid)


@socketio.on("register")
def register(data):
    sid = request.sid
    username = data.get('username', '').strip()
    email = data.get('email', '').strip()
    password = data.get('password', '').strip()

    if username == '' or email == '' or password == '':
        socketio.emit('failed-login', 'fields username, email and password cannot be empty', to=sid)
        return

    user = check_is_email_exist(email)
    if user is not None:
        socketio.emit('failed-login', 'user with this email exist', to=sid)
        return

    code = create_user_code(4)
    new_user = create_new_user(username, email, password, code)
    token = create_token(8)
    new_connection = create_new_connection(sid, token, new_user.id, datetime.now())
    socketio.emit('success-login', {'email': email, 'username': username, 'userCode': code, 'token': token}, to=sid)


@socketio.on('logout')
def logout(data):
    token = data.get('token', '').strip()
    delete_connection_by_token(token)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    socketio.run(app, debug=True, port=5000, allow_unsafe_werkzeug=True)
