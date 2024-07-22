from flask import request

from app.lock import requires_lock
from app.query import get_user_by_sid, get_every_invitations_for_user_id, get_user_by_user_id, \
    get_every_friends_id_for_user_id, accept_invitation_by_users_id, decline_invitation_by_users_id, \
    get_conv_id_by_users_id, get_user_by_username_and_code, invite_friend_by_users_id


def create_friends_list_routes(socketio):
    @socketio.on('get_invitations')
    @requires_lock
    def get_invitations():
        invitations = get_every_invitations_for_user_id(get_user_by_sid(request.sid).id)
        user_invitations = []
        for x in invitations:
            user = get_user_by_user_id(x)
            user_invitations.append({'id': user.id, 'username': user.username, 'userCode': user.code, 'email': user.email})
        socketio.emit('invitations_list', user_invitations)

    @socketio.on('get_friends_list')
    @requires_lock
    def get_friends_list():
        friends_id_list = get_every_friends_id_for_user_id(get_user_by_sid(request.sid).id)
        user_friends_list = []
        for x in friends_id_list:
            user = get_user_by_user_id(x)
            user_friends_list.append({'id': user.id, 'username': user.username, 'userCode': user.code, 'email': user.email, 'conv_id': get_conv_id_by_users_id(user.id, get_user_by_sid(request.sid).id)})
        socketio.emit('friends_list', user_friends_list, to=request.sid)

    @socketio.on('add_new_invitation')
    @requires_lock
    def add_new_invitation(inputValue):
        username = inputValue.split('#')[0]
        code = inputValue.split('#')[1]
        user = get_user_by_username_and_code(username, code)
        print(user)
        if user is None:
            # nie mozna dodac
             return
        invite_friend_by_users_id(get_user_by_sid(request.sid).id, user.id)
        user_invitations = get_every_invitations_for_user_id(user.id)
        socketio.emit('invitations_list', user_invitations)

    @socketio.on('accept_invitation')
    @requires_lock
    def accept_invitation(id):
        user = get_user_by_sid(request.sid)
        accept_invitation_by_users_id(id, user.id)

        # NIE POWINNO BYC POTRZEBNE PRZY SOCKET
        get_invitations()
        get_friends_list()

    @socketio.on('decline_invitation')
    @requires_lock
    def decline_invitation(id):
        user = get_user_by_sid(request.sid)
        decline_invitation_by_users_id(id, user.id)

        # NIE POWINNO BYC POTRZEBNE PRZY SOCKET
        get_invitations()
        get_friends_list()
