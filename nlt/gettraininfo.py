import requests

api_url = 'https://indian-railway-api.cyclic.app/trains/getTrain/?trainNo={train_no}'

def query1(train_no):
    formatted_url = f'{api_url.format(train_no=train_no)}'
    response = requests.get(formatted_url)
    data = response.json()
    return data



# print(query1("22666"))