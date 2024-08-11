from datetime import datetime

from lib.hash import hash_password
from lib import db
from .models import User, Connection, FriendsRelation, Message, Invite


# USER TABLE
def check_is_email_exist(email):
    user = User.query.filter_by(email=email).first()
    return user if user else None


def create_new_user(username, email, password, code):
    new_user = User(username, email, hash_password(password), code)
    db.session.add(new_user)
    db.session.commit()
    return new_user


def get_user_by_sid(sid):
    connection = Connection.query.filter_by(sid=sid).first()
    if connection:
        user = User.query.filter_by(id=connection.user_id).first()
        if user:
            return user
    return None


def get_user_by_user_id(id):
    user = User.query.filter_by(id=id).first()
    return user if user else None


def get_user_by_username_and_code(username, code):
    user = User.query.filter_by(username=username, code=code).first()
    return user if user else None


# CONNECTION
def create_new_connection(sid, token, user_id, data):
    new_connection = Connection(sid, token, user_id, data)
    db.session.add(new_connection)
    db.session.commit()
    return new_connection


def get_connection_by_token_if_exist_connect(token, new_sid):
    connection = Connection.query.filter_by(token=token).first()
    if connection:
        connection.sid = new_sid
        db.session.commit()
        return connection
    return None


def delete_connection_by_token(token):
    connection = Connection.query.filter_by(token=token).first()
    if connection:
        db.session.delete(connection)
        db.session.commit()
        return True
    return False


def get_sid_by_user_id(user_id):
    connections = Connection.query.filter_by(user_id=user_id).all()
    connections_sid = []
    for connection in connections:
        connections_sid.append(connection.sid)
    return connections_sid


# FRIENDS RELATIONS
def get_every_friends_id_for_user_id(user_id):
    relations1 = FriendsRelation.query.filter_by(user1_id=user_id).all()
    relations2 = FriendsRelation.query.filter_by(user2_id=user_id).all()

    friends_id = []
    for relation in relations1:
        friends_id.append(relation.user2_id)
    for relation in relations2:
        friends_id.append(relation.user1_id)
    friends_id = list(set(friends_id))

    return friends_id


def get_conv_id_by_users_id(user_1_id, user_2_id):
    relations1 = FriendsRelation.query.filter_by(user1_id=user_1_id, user2_id=user_2_id).first()
    relations2 = FriendsRelation.query.filter_by(user2_id=user_1_id, user1_id=user_2_id).first()
    return relations1.id if relations1 else relations2.id


def get_every_invitations_for_user_id(user_id):
    invitations = Invite.query.filter_by(invitee_user_id=user_id).all()
    invitations_users_list = []
    for invitation in invitations:
        invitations_users_list.append(invitation.inviter_user_id)
    return invitations_users_list


def accept_invitation_by_users_id(user1_id, user2_id):
    invitation = Invite.query.filter_by(inviter_user_id=user1_id, invitee_user_id=user2_id).first()
    if invitation:
        db.session.delete(invitation)
        date = datetime.now()
        friend_relation = FriendsRelation(user1_id, user2_id, date)
        db.session.add(friend_relation)
        db.session.commit()

        return friend_relation


def decline_invitation_by_users_id(user1_id, user2_id):
    invitation = Invite.query.filter_by(inviter_user_id=user1_id, invitee_user_id=user2_id).first()
    if invitation:
        db.session.delete(invitation)
        db.session.commit()


def invite_friend_by_users_id(inviter_user_id, invitee_user_id):
    invitation = Invite.query.filter_by(inviter_user_id=inviter_user_id, invitee_user_id=invitee_user_id).first()
    if invitation:
        return {'message': "User already invited"}

    invitation = Invite.query.filter_by(inviter_user_id=invitee_user_id, invitee_user_id=inviter_user_id).first()
    if invitation:
        return {'message': "You are already invited"}

    invitation = Invite(inviter_user_id, invitee_user_id, datetime.now())
    db.session.add(invitation)
    db.session.commit()
    return {'invitation': invitation, 'message': "success"}


# MESSAGES
def create_new_message(conversation_id, message, user_id):
    new_message = Message(conversation_id, user_id, message, datetime.now())
    db.session.add(new_message)
    db.session.commit()
    return new_message.to_dict()


def get_every_messages_for_conversation_id(conversation_id):
    messages = Message.query.filter_by(conversation_id=conversation_id).all()
    messages_dict = []
    for message in messages:
        message_dict = message.to_dict()
        message_dict['username'] = get_user_by_user_id(message.who_send_user_id).username
        messages_dict.append(message_dict)
    return messages_dict


# conversation
def get_conversation_id_by_users_id(user1_id, user2_id):
    con1 = FriendsRelation.query.filter_by(user1_id=user1_id, user2_id=user2_id).first()
    con2 = FriendsRelation.query.filter_by(user1_id=user2_id, user2_id=user1_id).first()
    if con1:
        return con1.id
    if con2:
        return con2.id


def get_conversation_by_id(conversation_id):
    conv = FriendsRelation.query.filter_by(id=conversation_id).first()
    return conv if conv else None