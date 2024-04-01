import requests

url = "https://current-affairs-of-india.p.rapidapi.com/history-of-today"

headers = {
	"X-RapidAPI-Key": "2c0ed6f314mshbb65dbdd138bbbbp1b2145jsnd8bd8da15c79",
	"X-RapidAPI-Host": "current-affairs-of-india.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())