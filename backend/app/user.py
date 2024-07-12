import random


class User:
    def __init__(self, username: str, email: str, password: str, sid: str):
        self.connected = False
        self.username = username
        self.email = email
        self.password = password
        self.userCode = str(random.randint(0, 999)).zfill(3)
        self.sid = sid

    def connect(self):
        self.connected = True

    def disconnect(self):
        self.connected = False

    def is_connected(self):
        return self.connected

    def try_to_login(self, email: str, password: str):
        if self.email == email:
            if self.password == password:
                return {'succeed': True, 'message': 'Login successful!'}
            else:
                return {'succeed': False, 'message': 'Wrong password!'}
        else:
            return {'succeed': False, 'message': 'Wrong email!'}

    def __str__(self):
        return f'USER: {self.username}, {self.email}, {self.sid}, {self.connected}'


users = {
    'admin': User('admin', 'admin@admin', 'admin', 'admin'),
    'a': User('a', 'a@a', 'a', 'a'),
    'b': User('b', 'b@b', 'b', 'b'),
}
