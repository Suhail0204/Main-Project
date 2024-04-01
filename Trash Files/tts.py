# import requests

# url = "https://text-to-speech-api3.p.rapidapi.com/speak"

# querystring = {"text":"hello world","lang":"en"}

# headers = {
# 	"X-RapidAPI-Key": "2c0ed6f314mshbb65dbdd138bbbbp1b2145jsnd8bd8da15c79",
# 	"X-RapidAPI-Host": "text-to-speech-api3.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers, params=querystring)

# print(response.json())

# import requests

# url = "https://text-to-speech-api3.p.rapidapi.com/speak"

# querystring = {"text": "hello world", "lang": "en"}

# headers = {
#     "X-RapidAPI-Key": "2c0ed6f314mshbb65dbdd138bbbbp1b2145jsnd8bd8da15c79",
#     "X-RapidAPI-Host": "text-to-speech-api3.p.rapidapi.com"
# }

# try:
#     response = requests.get(url, headers=headers, params=querystring)
#     response.raise_for_status()  # Raise an exception for bad responses (4xx and 5xx)

#     # Check if the response contains JSON data
#     try:
#         data = response.json()
#         print(data)
#     except ValueError:
#         print("Response is not in JSON format:")

# except requests.exceptions.RequestException as e:
#     print("Error making API request:", e)


import requests

url = "https://text-to-speech-api3.p.rapidapi.com/speak"

querystring = {"text": "hello world", "lang": "en"}

headers = {
    "X-RapidAPI-Key": "2c0ed6f314mshbb65dbdd138bbbbp1b2145jsnd8bd8da15c79",
    "X-RapidAPI-Host": "text-to-speech-api3.p.rapidapi.com"
}

try:
    response = requests.get(url, headers=headers, params=querystring)
    response.raise_for_status()  # Raise an exception for bad responses (4xx and 5xx)

    # Save the audio content to a file
    with open("output_audio.mp3", "wb") as f:
        f.write(response.content)

    print("Audio output saved to output_audio.mp3")

except requests.exceptions.RequestException as e:
    print("Error making API request:", e)
