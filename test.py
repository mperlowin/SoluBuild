import base64
import json
import logging

from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
app.config["DEBUG"] = True
socketio = SocketIO(app)

HTTP_SERVER_PORT = 5000

@socketio.on('connect')
def handle_connect():
    app.logger.info("Connection accepted")
    print("Connection accepted")

@socketio.on('message')
def handle_message(message):
    app.logger.info("Connected Message received: {}".format(message))
    # A lot of messages will be sent rapidly. We'll stop showing after the first one.
    has_seen_media = False
    message_count = 0

    # Messages are a JSON encoded string
    data = json.loads(message)

    # Using the event type you can determine what type of message you are receiving
    if data['event'] == "connected":
        app.logger.info("Connected Message received: {}".format(message))
    if data['event'] == "start":
        app.logger.info("Start Message received: {}".format(message))
    if data['event'] == "media":
        if not has_seen_media:
            app.logger.info("Media message: {}".format(message))
            payload = data['media']['payload']
            app.logger.info("Payload is: {}".format(payload))
            chunk = base64.b64decode(payload)
            app.logger.info("That's {} bytes".format(len(chunk)))
            app.logger.info("Additional media messages from WebSocket are being suppressed....")
            has_seen_media = True
    if data['event'] == "closed":
        app.logger.info("Closed Message received: {}".format(message))
        socketio.disconnect()

    message_count += 1

    app.logger.info("Received a total of {} messages".format(message_count))

@socketio.on('disconnect')
def handle_disconnect():
    app.logger.info("Connection closed.")

if __name__ == '__main__':
    app.logger.setLevel(logging.DEBUG)
    print("Server listening on: http://localhost:" + str(HTTP_SERVER_PORT))
    socketio.run(app, port=HTTP_SERVER_PORT)
