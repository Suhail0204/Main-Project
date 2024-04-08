import requests

def get_train_route(train_no):
    url = f"https://indian-railway-api.cyclic.app/trains/getRoute?trainNo={train_no}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Example usage:
train_no = 19034
route_data = get_train_route(train_no)
if route_data:
    print(route_data)
else:
    print("Failed to fetch train route data.")
