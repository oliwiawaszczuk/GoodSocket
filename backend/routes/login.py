from flask import request

from app.user import users, User


def create_login_routes(socketio):
    @socketio.on('auto_login')
    def auto_login(token):
        if token in users:
            user = users[token]
            socketio.emit('success-login', {'username': user.username, 'userCode': user.userCode, 'sid': request.sid}, to=request.sid)
            users[request.sid] = users.pop(token)

    @socketio.on('login')
    def login(data):
        sid = request.sid
        email = data['email'].strip()
        password = data['password'].strip()
        if email == '' or password == '':
            socketio.emit('failed-login', 'fields email and password cannot be empty', to=sid)
        else:
            user = next((u for u in users.values() if u.email == email), None)
            if user:
                login_result = user.try_to_login(email, password)
                if login_result['succeed']:
                    user.connect()
                    users[sid] = user
                    old_sid = user.sid
                    user.sid = sid
                    if old_sid in users:
                        del users[old_sid]
                    socketio.emit('success-login',
                                  {'email': email, 'username': user.username, 'userCode': user.userCode, 'sid': sid},
                                  to=sid)
                else:
                    socketio.emit('failed-login', login_result['message'], to=sid)
            else:
                socketio.emit('failed-login', 'account with this email does not exist', to=sid)

    @socketio.on('register')
    def register(data):
        sid = request.sid
        username = data['username'].strip()
        email = data['email'].strip()
        password = data['password'].strip()
        if email == '' or password == '' or username == '':
            socketio.emit('failed-login', 'fields email and password cannot be empty', to=sid)
        elif any(user.email == email for user in users.values()):
            socketio.emit('failed-login', 'email already exists', to=sid)
        else:
            new_user = User(username, email, password, sid)
            users[sid] = new_user
            new_user.connect()
            socketio.emit('success-login',
                          {'email': email, 'username': username, 'userCode': new_user.userCode, 'sid': sid}, to=sid)