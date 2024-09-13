# chat/consumers.py
import json
import base64
from channels.generic.websocket import WebsocketConsumer
import numpy as np
import librosa
import datetime
from queue import Queue
import whisper


model = whisper.load_model("tiny")

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.audio_buffer = np.zeros(4096, dtype=np.float32)  # Initialize a buffer

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        data = json.loads(text_data)
        event = data.get('event')

        def handle_media():
            payload = data.get('media').get('payload')
            chunk = base64.b64decode(payload)
            print(f"Received chunk of size {len(chunk)}")

            # Convert the µ-law chunk to PCM
            ulaw_data = np.frombuffer(chunk, dtype=np.uint8)
            pcm_data = (ulaw_data.astype(np.float32) - 128.0) / 128.0  # Convert to float in range [-1, 1]

            # Add the PCM data to the buffer
            self.audio_buffer[:-len(pcm_data)] = self.audio_buffer[len(pcm_data):]
            self.audio_buffer[-len(pcm_data):] = pcm_data

            # Process the buffer to generate log-mel spectrogram
            sr = 8000
            n_mels = 128
            hop_length = 512
            n_fft = 2048

            S = librosa.feature.melspectrogram(y=self.audio_buffer, sr=sr, n_fft=n_fft, hop_length=hop_length, n_mels=n_mels)
            log_S = librosa.power_to_db(S, ref=np.max)
            result = whisper.transcribe(model, log_S)
            print(result)

            # Send back a confirmation or the spectrogram data if needed
            self.send(text_data=json.dumps({"message": 'Log-mel spectrogram generated'}))
        
        def handle_default():
            print('Default event received')
            self.send(text_data=json.dumps({"message": 'Default event received'}))

        event_handler = {
            "media": handle_media,
        }
        
        handler = event_handler.get(event, handle_default)
        response_message = handler()

        self.send(text_data=json.dumps({"message": response_message}))
