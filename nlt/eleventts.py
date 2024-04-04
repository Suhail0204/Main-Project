import requests



def tts(text):
    url = "https://api.elevenlabs.io/v1/text-to-speech/Mu5jxyqZOLIGltFpfalg"
    payload = {
    "model_id": "eleven_monolingual_v1",
    "text": text,
    # "voice_settings": {
    #     "stability": 2,
    #     "similarity_boost": 2
    # }
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
        with open("static/output.mp3", "wb") as f:
            f.write(audio_content)
        
        print("Audio saved to output.mp3")
    else:
        print(f"Error: {response.status_code} - {response.text}")

