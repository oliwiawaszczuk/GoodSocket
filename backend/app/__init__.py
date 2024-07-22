from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO
import os

db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../data/database.db"))


def create_app(db, migrate):
    app = Flask(__name__)
    CORS(app, supports_credentials=True)
    socketio = SocketIO(app, cors_allowed_origins="*")

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    from routes.socket import create_socket_routes
    from routes.login import create_login_routes
    from routes.message import create_message_routes
    from routes.friendsList import create_friends_list_routes

    create_socket_routes(socketio)
    create_login_routes(socketio)
    create_message_routes(socketio)
    create_friends_list_routes(socketio)

    return app, socketio
