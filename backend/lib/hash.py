from hashlib import sha1


def hash_password(password):
    return sha1(password.encode()).digest()
    import bcrypt
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def verify_password(password, hashed_password):
    return sha1(password.encode()).digest() == hashed_password
    import bcrypt
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
