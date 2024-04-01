# # # import espeakng
# # # from django.http import HttpResponse

# # # # Initialize the espeak-ng synthesizer
# # # synth = espeakng.Synth()

# # # # Set the language
# # # synth.set_voice("en")

# # # # Set the text you want to convert to speech
# # # text = "Hello, how are you?"

# # # # Synthesize the text to speech
# # # audio_data = synth.synth_wav(text)

# # # # Close the synthesizer
# # # synth.close()

# # import pyttsx3
# # text_speech = pyttsx3.init()
# # answer = "வணக்கம் உங்களுக்கு என் உதவி எப்படி இருக்கிறது"
# # text_speech.say(answer)
# # text_speech.runAndWait()

# # import requests

# # API_URL = "https://api-inference.huggingface.co/models/openai/whisper-large-v3"
# # headers = {"Authorization": "Bearer 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"}

# # def query(filename):
# #     with open(filename, "rb") as f:
# #         data = f.read()
# #     response = requests.post(API_URL, headers=headers, data=data)
# #     return response.json()

# # output = query("sample1.flac")

# import requests

# API_URL = "https://api-inference.huggingface.co/models/Dubverse/MahaTTS"
# headers = {"Authorization": "Bearer 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"}

# def query(payload):
# 	response = requests.post(API_URL, headers=headers, json=payload)
# 	return response.content

# audio_bytes = query({
# 	"inputs": "The answer to the universe is 42",
# })

# audio_path = "static/output.wav"
# with open(audio_path, "wb") as audio_file:
#     audio_file.write(audio_bytes)


import requests
import io
from pydub import AudioSegment

API_URL = "https://api-inference.huggingface.co/models/Dubverse/MahaTTS"
headers = {"Authorization": "Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content

# Input text
text_input = "The answer to the universe is 42"

# Make a request to the Hugging Face Inference API
audio_bytes = query({"inputs": text_input})

# Convert the audio to an AudioSegment
audio = AudioSegment.from_wav(io.BytesIO(audio_bytes))

# Convert the AudioSegment to MP3 format
mp3_data = audio.export(format="mp3").read()

# Save the MP3 file locally (adjust the path as needed)
mp3_path = "static/output.mp3"
with open(mp3_path, "wb") as mp3_file:
    mp3_file.write(mp3_data)
