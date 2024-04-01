import requests

url = "https://rstations.p.rapidapi.com/"

payload = { "search": "Delhi" }
headers = {
	"content-type": "application/json",
	"Content-Type": "application/json",
	"X-RapidAPI-Key": "2c0ed6f314mshbb65dbdd138bbbbp1b2145jsnd8bd8da15c79",
	"X-RapidAPI-Host": "rstations.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())