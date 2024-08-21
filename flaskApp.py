import os
from flask import Flask, request, jsonify, Response, render_template
from flask_sockets import Sockets
from twilio.twiml.voice_response import Connect, VoiceResponse, Say, Start, Stream
import ngrok
import asyncio
import nest_asyncio
import signal
import logging
import json
import base64
try:
    from google.colab import userdata
    IN_COLAB = True
except ImportError:
    IN_COLAB = False
    from dotenv import load_dotenv
    load_dotenv()

app = Flask(__name__)
sockets = Sockets(app)

class FlaskApp:
    def __init__(self):
        # Initialize Flask app
        self.app = app
        self.port = 5000
        self.setup_routes()
        nest_asyncio.apply()
        asyncio.get_event_loop().run_until_complete(self.setup_ngrok())
        self.start_flask_app()

    def setup_routes(self):
        @self.app.route('/', methods=['GET'])
        def home():
            return "Hello, World!"
        
        @self.app.route('/test', methods=['POST'])
        def test():
            data = request.data
            print(f"Data received: {data}")
            return jsonify({"message": "Data received successfully"}), 200
        
        @self.app.route('/twiml', methods=['POST'])
        def return_twiml():
            response = VoiceResponse()
            connect = Connect()
            connect.stream(url=f'{self.listener.url().replace('https', 'wss')}/audio')
            response.append(connect)
            response.say(
                'cash cash money hoe'
            )
            print(response)
            return Response(str(response), mimetype='text/xml')

        @sockets.route('/audio')
        def echo(ws):
            app.logger.info("Connection accepted")
            # A lot of messages will be sent rapidly. We'll stop showing after the first one.
            has_seen_media = False
            message_count = 0
            while not ws.closed:
                message = ws.receive()
                if message is None:
                    app.logger.info("No message received...")
                    continue
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
                    break
                message_count += 1
        
        @self.app.route('/shutdown', methods=['POST', 'GET'])
        async def shutdown():
            await self.listener.close()
            print("Tunnel closed.")
            shutdown_server()
            return 'Server shutting down...'
    
    async def setup_ngrok(self):
        token = userdata.get("NGROK_AUTHTOKEN") if IN_COLAB else os.getenv("NGROK_AUTHTOKEN")
        ngrok.set_auth_token(token)
        self.listener = await ngrok.forward(f"localhost:{self.port}")
        print(f"Ingress established at {self.listener.url()}")
            

    def start_flask_app(self):
        self.app.logger.setLevel(logging.DEBUG)
        from gevent import pywsgi
        from geventwebsocket.handler import WebSocketHandler
        server = pywsgi.WSGIServer(('', self.port), app, handler_class=WebSocketHandler)
        print("Server listening on: http://localhost:" + str(self.port))
        server.serve_forever()

def shutdown_server():
    pid = os.getpid()
    os.kill(pid, signal.SIGINT)

import threading

FlaskApp()