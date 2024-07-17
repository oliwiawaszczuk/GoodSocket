from flask import Flask, request
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

users = {}


@socketio.on('connect')
def connect():
    sid = request.sid
    print(f"connected sid: {sid}")
    users[sid] = {'connected': True, 'sid': sid}
    # for user in users:
    #     print(user)


@socketio.on('disconnect')
def disconnect():
    sid = request.sid
    print(f"disconnected sid: {sid}")
    users[sid]['connected'] = False
    # if sid in users:
    #     users.pop(sid)


@socketio.on('message')
def message(_message):
    sid = request.sid
    print(f"message {_message}, from sid: {sid} and user: {users[sid]}")


@socketio.on('auto_login')
def auto_login(token):
    sid = request.sid
    if token:
        print(f'try to auth login with token {token}')
        if token == 'admin':
            print('login to admin')
            login({'email': 'admin', 'password': 'admin'}, sid)
        if token in users:
            print(users[token])
            login({'email': users[token]['email'], 'password': users[token]['password']}, sid)


@socketio.on('login')
def login(data, sid=None):
    if sid is None:
        sid = request.sid
    email = data.get('email', '').strip()
    password = data.get('password', '').strip()
    if email == '' or password == '':
        socketio.emit('failed-login', 'fields email and password cannot be empty', to=sid)
    else:
        if sid in users:
            users[sid]['email'] = email
            users[sid]['password'] = password
            socketio.emit('success-login', {'email': email, 'username': 'user/name', 'userCode': 444, 'sid': sid}, to=sid)
        else:
            print(f"No user data found for sid {sid}")


@socketio.on("register")
def register(data):
    sid = request.sid
    username = data.get('username', '').strip()
    email = data.get('email', '').strip()
    password = data.get('password', '').strip()

    if email == '' or password == '':
        socketio.emit('failed-login', 'fields email and password cannot be empty', to=sid)
        return

    users[sid] = {
        "username": username,
        "email": email,
        "password": password
    }
    socketio.emit('success-login', {'email': email, 'username': 'user/name', 'userCode': 444, 'sid': sid}, to=sid)


if __name__ == '__main__':
    socketio.run(app, port=5000, allow_unsafe_werkzeug=True, debug=True)
