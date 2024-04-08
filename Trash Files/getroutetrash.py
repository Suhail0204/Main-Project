from requests import get

class YourClassName:
    def getRoute(self, TN):
        # Retrieve Train ID
        ID = self.getTrain(TN)
        try:
            # Check if there was an error in retrieving train details
            error = ID.get('error')
            if error:
                return {"error": error}  # Return error message if present
            else:
                # Extract train ID
                train_id = ID['train_base']['train_id']
        except KeyError:
            return {"error": "Train ID not found"}

        # Build URL
        URL_Route = f"https://erail.in/data.aspx?Action=TRAINROUTE&Password=2012&Data1={train_id}&Data2=0&Cache=true"

        # Retrieve Route Information
        response = get(URL_Route)
        if response.status_code != 200:
            return {"error": f"Failed to fetch route information. Status code: {response.status_code}"}

        # Return Route Information as JSON
        return Prettify().StationToJson(response.text)

# Instantiate your class
your_instance = YourClassName()

# Call the getRoute function with the train number 12345
route_info = your_instance.getRoute(22666)

# Print the output
print(route_info)
