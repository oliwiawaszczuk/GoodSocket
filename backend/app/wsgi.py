from flask import Flask, request
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")


user_data = {}


@socketio.on('connect')
def connect():
    print(f"connected sid: {request.sid}")
    user_data['connected'] = True
    user_data['sid'] = request.sid


@socketio.on('disconnect')
def disconnect():
    print(f"disconnected sid: {request.sid}")
    user_data['connected'] = False
    user_data['sid'] = None


@socketio.on('message')
def message(message):
    print(f"message {message}, from sid: {request.sid} and user sid: {user_data['sid']}")


if __name__ == '__main__':
    socketio.run(app, port=5000, allow_unsafe_werkzeug=True, debug=True)
