# import requests

# url = "https://indianrailways.p.rapidapi.com/index.php"

# querystring = {"pnr":"1234567890"}

# headers = {
# 	"X-RapidAPI-Key": "2c0ed6f314mshbb65dbdd138bbbbp1b2145jsnd8bd8da15c79",
# 	"X-RapidAPI-Host": "indianrailways.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers, params=querystring)

# print(response.json())

import requests

url = "https://indianrailways.p.rapidapi.com/index.php"

querystring = {"pnr":"1234567890"}

headers = {
    "X-RapidAPI-Key": "2c0ed6f314mshbb65dbdd138bbbbp1b2145jsnd8bd8da15c79",
    "X-RapidAPI-Host": "indianrailways.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

# Print the response content to inspect it
print(response.text)
