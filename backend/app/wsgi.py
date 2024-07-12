from flask import Flask, request
from flask_socketio import SocketIO

from routes.login import create_login_routes
from user import User, users

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")


@socketio.on('connect')
def connect():
    sid = request.sid
    print(f"connected sid: {sid}")
    users[sid] = User('', '', '', sid)
    for x in users:
        print(users[x].__str__())


@socketio.on('disconnect')
def disconnect():
    sid = request.sid
    print(f"disconnected sid: {sid}")
    if sid in users:
        users[sid].disconnect()


@socketio.on('message')
def message(message):
    sid = request.sid
    print(f'USERS: {users}')
    print(f"message {message}, from sid: {sid} and user: {users[sid]}")


if __name__ == '__main__':
    b_user = User('b', 'b@b', 'b', 'b')
    users['b'] = b_user

    create_login_routes(socketio)
    socketio.run(app, port=5000, allow_unsafe_werkzeug=True, debug=True)
