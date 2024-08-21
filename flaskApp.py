import os
from flask import Flask, request, jsonify, Response
from twilio.twiml.voice_response import VoiceResponse
import ngrok
import asyncio
import nest_asyncio
import signal
try:
    from google.colab import userdata
    IN_COLAB = True
except ImportError:
    IN_COLAB = False
    from dotenv import load_dotenv
    load_dotenv()

class FlaskApp:
    def __init__(self):
        # Initialize Flask app
        self.app = Flask(__name__)
        self.port = 5000
        self.setup_routes()
        nest_asyncio.apply()
        asyncio.get_event_loop().run_until_complete(self.setup_ngrok())
        self.start_flask_app()

    def setup_routes(self):
        @self.app.route('/', methods=['GET'])
        def home():
            return "Hello, World!"
        
        @self.app.route('/twiml', methods=['GET', 'POST'])
        def twiml():
            response = VoiceResponse()
            response.stream(url=self.listener.url().replace("https", "wss") + "/audio")
            return Response(str(response), mimetype='text/xml')

        @self.app.route('/audio', methods=['POST'])
        def process_audio():
            data = request.data
            with open('audio_stream.raw', 'wb') as f:
                f.write(data)
            return jsonify({"message": "Data received successfully"}), 200
        
        @self.app.route('/shutdown', methods=['POST', 'GET'])
        async def shutdown():
            await self.listener.close()
            print("Tunnel closed.")
            shutdown_server()
            return 'Server shutting down...'
    
    async def setup_ngrok(self):
        token = userdata.get("") if IN_COLAB else os.getenv("")
        ngrok.set_auth_token(token)
        self.listener = await ngrok.forward(f"localhost:{self.port}")
        print(f"Ingress established at {self.listener.url()}")
            

    def start_flask_app(self):
        self.app.run(port=self.port)
        print(f"Flask app running on port: {self.port}.")

def shutdown_server():
    pid = os.getpid()
    os.kill(pid, signal.SIGINT)

import threading

# Global variable to store the FlaskApp instance lol
flask_app_instance = None

def run_flask_app():
    global flask_app_instance
    flask_app_instance = FlaskApp()

# Create a thread targeting the run_flask_app function
flask_thread = threading.Thread(target=run_flask_app)

# Start the thread
flask_thread.start()