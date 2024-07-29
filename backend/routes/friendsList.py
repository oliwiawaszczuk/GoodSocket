from flask import request

from app.lock import requires_lock
from app.query import get_user_by_sid, get_every_invitations_for_user_id, get_user_by_user_id, \
    get_every_friends_id_for_user_id, accept_invitation_by_users_id, decline_invitation_by_users_id, \
    get_conv_id_by_users_id, get_user_by_username_and_code, invite_friend_by_users_id, get_sid_by_user_id


def create_friends_list_routes(socketio):
    @socketio.on('get_invitations')
    @requires_lock
    def get_invitations(sid=None):
        if sid is None:
            sid = request.sid
        invitations = get_every_invitations_for_user_id(get_user_by_sid(request.sid).id)
        user_invitations = []
        for x in invitations:
            user = get_user_by_user_id(x)
            user_invitations.append(
                {'id': user.id, 'username': user.username, 'userCode': user.code, 'email': user.email})
        socketio.emit('invitations_list', user_invitations, to=sid)

    @socketio.on('get_friends_list')
    @requires_lock
    def get_friends_list(sid=None):
        if sid is None:
            sid = request.sid
        friends_id_list = get_every_friends_id_for_user_id(get_user_by_sid(sid).id)
        user_friends_list = []
        for x in friends_id_list:
            user = get_user_by_user_id(x)
            user_friends_list.append(
                {'id': user.id, 'username': user.username, 'userCode': user.code, 'email': user.email,
                 'conv_id': get_conv_id_by_users_id(user.id, get_user_by_sid(sid).id)})
        socketio.emit('friends_list', user_friends_list, to=sid)

    @socketio.on('add_new_invitation')
    @requires_lock
    def add_new_invitation(inputValue: str):
        if inputValue.count("#") != 1:
            socketio.emit('failed_request_end_with_error', 'After # must be code', to=request.sid)
            return

        username = inputValue.strip().split('#')[0]
        code = inputValue.strip().split('#')[1]
        user = get_user_by_username_and_code(username, str(code))
        if user is None:
            socketio.emit('failed_request_end_with_error', 'User does not exist', to=request.sid)
            return

        msg = invite_friend_by_users_id(get_user_by_sid(request.sid).id, user.id)
        if msg != "success":
            socketio.emit('failed_request_end_with_error', msg, to=request.sid)
            return

        user_invitations = get_every_invitations_for_user_id(user.id)
        socketio.emit('invitations_list', user_invitations, to=get_sid_by_user_id(user.id))

    @socketio.on('accept_invitation')
    @requires_lock
    def accept_invitation(id):
        user = get_user_by_sid(request.sid)
        friend_relation = accept_invitation_by_users_id(id, user.id)

        get_invitations(request.sid)
        get_friends_list(request.sid)

        ids = get_sid_by_user_id(id)
        for id in ids:
            get_friends_list(id)

    @socketio.on('decline_invitation')
    @requires_lock
    def decline_invitation(id):
        user = get_user_by_sid(request.sid)
        decline_invitation_by_users_id(id, user.id)

        get_invitations(request.sid)
