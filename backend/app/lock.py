from threading import Lock

from flask import request

chat_lock = Lock()


def requires_lock(fn):
    def _fn(*args, **kwargs):
        try:
            print(f"request from user with sid {request.sid}")
            chat_lock.acquire()
            result = fn(*args, **kwargs)
            return result
        finally:
            chat_lock.release()
    return _fn
