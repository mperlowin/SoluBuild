from flask import Flask
from flask_socketio import SocketIO
from gevent import pywsgi
from geventwebsocket.handler import WebSocketHandler

app = Flask(__name__)
socketio = SocketIO(logger=True, engineio_logger=True)
socketio.init_app(app)

@socketio.on('connect')
def handle_connect():
    app.logger.info("Connection accepted")
    print("Connection accepted")

@socketio.on("message")
def message(data):
    print(data)
    socketio.emit("myevent", "EVENT DATA HERE...")

# @socketio.on('disconnect')
# def handle_disconnect():
#     app.logger.info("Connection closed.")

if __name__ == "__main__":
    pywsgi.WSGIServer(("", 5000), app, handler_class=WebSocketHandler).serve_forever()