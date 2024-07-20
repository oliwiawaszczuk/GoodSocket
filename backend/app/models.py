from datetime import datetime, timedelta

from lib import db


class User(db.Model):
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
    id = db.Column(db.Integer, primary_key=True)
    sid = db.Column(db.String(120), nullable=False)
    token = db.Column(db.String(120), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
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