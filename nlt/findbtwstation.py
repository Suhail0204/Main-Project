import requests

api_url = 'https://indian-railway-api.cyclic.app/trains/betweenStations/?from={from_station}&to={to_station}'

def query_between_stations(from_station, to_station):
    formatted_url = api_url.format(from_station=from_station, to_station=to_station)
    response = requests.get(formatted_url)
    data = response.json()
    return data

# Example usage:
from_station = 'ST'
to_station = 'ANND'
output = query_between_stations(from_station, to_station)
print(output)
