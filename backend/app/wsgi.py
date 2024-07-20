from app import create_app
from lib import db, migrate

app, socketio = create_app(db, migrate)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    socketio.run(app, debug=True, port=5000, allow_unsafe_werkzeug=True)
