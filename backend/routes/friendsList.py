from flask import request

from app.lock import requires_lock
from app.query import get_user_by_sid, get_every_invitations_for_user_id, get_user_by_user_id, \
    get_every_friends_id_for_user_id, accept_invitation_by_users_id, decline_invitation_by_users_id, \
    get_conv_id_by_users_id, get_user_by_username_and_code, invite_friend_by_users_id, get_sid_by_user_id


def create_friends_list_routes(socketio):
    @socketio.on('get_invitations')
    def get_invitations(sid=None):
        if sid is None:
            sid = request.sid
        invitations = get_every_invitations_for_user_id(get_user_by_sid(sid).id)
        user_invitations = []
        for x in invitations:
            user = get_user_by_user_id(x)
            user_invitations.append(
                {'id': user.id, 'username': user.username, 'userCode': user.code, 'email': user.email})

        try:
            socketio.emit('invitations_list', user_invitations, to=sid)
        except Exception as e:
            raise e

    @socketio.on('get_friends_list')
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

        try:
            socketio.emit('friends_list', user_friends_list, to=sid)
        except Exception as e:
            raise e

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

        invitation = invite_friend_by_users_id(get_user_by_sid(request.sid).id, user.id)
        if invitation['message'] != "success":
            socketio.emit('failed_request_end_with_error', invitation['message'], to=request.sid)
            return

        invitee_user = get_user_by_user_id(invitation['invitation'].invitee_user_id)
        sids = get_sid_by_user_id(invitee_user.id)
        for sid in sids:
            get_invitations(sid)

    @socketio.on('accept_invitation')
    @requires_lock
    def accept_invitation(id):
        user = get_user_by_sid(request.sid)
        friend_relation = accept_invitation_by_users_id(id, user.id)

        get_invitations(request.sid)
        get_friends_list(request.sid)

        sids = get_sid_by_user_id(id)
        for sid in sids:
            get_friends_list(sid)

    @socketio.on('decline_invitation')
    @requires_lock
    def decline_invitation(id):
        user = get_user_by_sid(request.sid)
        decline_invitation_by_users_id(id, user.id)

        get_invitations(request.sid)
