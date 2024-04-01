# import requests

# url = "https://api.elevenlabs.io/v1/text-to-speech/Mu5jxyqZOLIGltFpfalg"

# payload = {
#     "model_id": "eleven_monolingual_v1",
#     "text": "यह एक पेड़ है",
#     "voice_settings": {
#         "stability": 0.5,
#         "similarity_boost": 1
#     }
# }
# headers = {
#     "xi-api-key": "456649b4c264770115d8872521f0fb83",
#     "Content-Type": "application/json"
# }

# response = requests.request("POST", url, json=payload, headers=headers)

# print(response.text)


# import requests

# CHUNK_SIZE = 1024
# url = "https://api.elevenlabs.io/v1/text-to-speech/<voice-id>"

# headers = {
#   "Accept": "audio/mpeg",
#   "Content-Type": "application/json",
#   "xi-api-key": "<xi-api-key>"
# }

# data = {
#   "text": "Born and raised in the charming south, 
#   I can add a touch of sweet southern hospitality 
#   to your audiobooks and podcasts",
#   "model_id": "eleven_monolingual_v1",
#   "voice_settings": {
#     "stability": 0.5,
#     "similarity_boost": 0.5
#   }
# }

# response = requests.post(url, json=data, headers=headers)
# with open('output.mp3', 'wb') as f:
#     for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
#         if chunk:
#             f.write(chunk)

import requests

url = "https://api.elevenlabs.io/v1/text-to-speech/Mu5jxyqZOLIGltFpfalg"

payload = {
    "model_id": "eleven_monolingual_v1",
    "text": "ரயில் எண் 22666 என்று நீங்கள் தேடினீர்கள். CBE SBC UDAY EXP என்ற அதிவேக ரயில், கோயம்புத்தூர்யிலிருந்து 05.45 மணியளவில் புறப்பட்டு 12.30 மணியளவில் கே.எஸ்.ஆர். பெங்களூருவில் வந்தது.",
    "voice_settings": {
        "stability": 2,
        "similarity_boost": 2
    }
}

headers = {
    "xi-api-key": "456649b4c264770115d8872521f0fb83",
    "Content-Type": "application/json"
}

# Send the request to the API
response = requests.post(url, json=payload, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Retrieve the audio content from the response
    audio_content = response.content
    
    # Save the audio content to an MP3 file
    with open("output2.mp3", "wb") as f:
        f.write(audio_content)
        
    print("Audio saved to output.mp3")
else:
    print(f"Error: {response.status_code} - {response.text}")

