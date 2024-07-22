from flask import request


def create_socket_routes(socketio):
    @socketio.on('connect')
    def connect():
        sid = request.sid
        print(f"connected sid: {sid}")

    @socketio.on('disconnect')
    def disconnect():
        sid = request.sid
        print(f"disconnected sid: {sid}")