from datetime import datetime, timedelta

from lib import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    code = db.Column(db.String(4), nullable=False)

    def __init__(self, username, email, password, code):
        self.username = username
        self.email = email
        self.password = password
        self.code = code

    def __repr__(self):
        return '<User %r>' % self.username


class Connection(db.Model):
    __tablename__ = 'connections'

    id = db.Column(db.Integer, primary_key=True)
    sid = db.Column(db.String(120), nullable=False)
    token = db.Column(db.String(120), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    date_of_connection = db.Column(db.DateTime, nullable=False)
    expiration_date = db.Column(db.DateTime, nullable=False)

    def __init__(self, sid, token, user_id, date_of_connection):
        self.sid = sid
        self.token = token
        self.user_id = user_id
        self.date_of_connection = date_of_connection
        self.expiration_date = date_of_connection + timedelta(days=4)

    def change_sid(self, new_sid):
        self.sid = new_sid

    def extend_time_of_expiration(self, days):
        self.expiration_date = datetime.now() + timedelta(days=days)

    def __repr__(self):
        return '<Connection %r>' % self.sid


class FriendsRelation(db.Model):
    __tablename__ = 'friends_relation'

    id = db.Column(db.Integer, primary_key=True)
    user1_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user2_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    date_of_creation = db.Column(db.DateTime)

    def __init__(self, user1_id, user2_id, date_of_creation):
        self.user1_id = user1_id
        self.user2_id = user2_id
        self.date_of_creation = date_of_creation

    def __repr__(self):
        return f'{self.id}. {self.user1_id} - {self.user2_id}'


class Invite(db.Model):
    __tablename__ = 'invates'

    id = db.Column(db.Integer, primary_key=True)
    inviter_user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    invitee_user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    date_of_invite = db.Column(db.DateTime)

    def __init__(self, inviter_user_id, invitee_user_id, date_of_invite):
        self.inviter_user_id = inviter_user_id
        self.invitee_user_id = invitee_user_id
        self.date_of_invite = date_of_invite

    def __repr__(self):
        return f'{self.id}. {self.inviter_user_id} - {self.invitee_user_id}'


class Message(db.Model):
    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key=True)
    conversation_id = db.Column(db.Integer, db.ForeignKey('friends_relation.id'))
    who_send_user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    message = db.Column(db.String)
    date_and_hour = db.Column(db.DateTime)

    def __init__(self, conversation_id, who_send_user_id, message, date_and_hour):
        self.conversation_id = conversation_id
        self.who_send_user_id = who_send_user_id
        self.date_and_hour = date_and_hour
        self.message = message

    def to_dict(self):
        return {
            'id': self.id,
            'date_and_hour': self.date_and_hour.isoformat() if self.date_and_hour else None,
            'message': self.message,
            'user_id': self.who_send_user_id,
            'conversation_id': self.conversation_id
        }

    def __repr__(self):
        return f'{self.id}. {self.conversation_id} - {self.message} - {self.date_and_hour}'
