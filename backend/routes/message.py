from flask import request

from app.query import get_user_by_sid, create_new_message, get_every_messages_for_conversation_id, get_user_by_user_id


def create_message_routes(socketio):
    @socketio.on('add_new_message')
    def add_new_message(data):
        print(data, data.get('conv_id'))
        new_message = create_new_message(int(data.get('conv_id')), data.get('text'), get_user_by_sid(request.sid).id)
        new_message['username'] = get_user_by_sid(request.sid).username
        socketio.emit('add_new_message', new_message, to=request.sid)

    @socketio.on('message')
    def message(conv_id):
        messages = get_every_messages_for_conversation_id(conv_id)
        socketio.emit('message', {'conv_id': conv_id, 'messages': messages}, to=request.sid)
