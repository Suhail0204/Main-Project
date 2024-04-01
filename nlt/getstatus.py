import requests
from json import loads

class YourClass:
    def getStatus(self, TN, DD, MMM, YYYY, STN):
        D = '-'.join([str(DD), MMM, str(YYYY)])
        URL_Live = f"https://data.erail.in/getIR.aspx?&jsonp=true&Data=RUNSTATUS~0_{TN}_{D}_{STN}"
        response = requests.get(URL_Live)
        if response.status_code == 200:
            return loads(response.text.strip('()'))
        else:
            # Handle the case when the request fails
            print(f"Failed to fetch status. Status code: {response.status_code}")
            return None

# Create an instance of YourClass
your_instance = YourClass()

# Call the getStatus method on the instance
print(your_instance.getStatus(22666, 22, "mar", 2024, "ED"))
