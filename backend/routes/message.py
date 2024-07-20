from flask import request

from app.query import get_user_by_sid


def create_message_routes(socketio):
    @socketio.on('message')
    def message(_message):
        sid = request.sid
        print(f"message {_message}, from sid: {sid} and user: {get_user_by_sid(sid)}")