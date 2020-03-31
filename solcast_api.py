import requests
import json

url = 'https://api.solcast.com.au/world_pv_power/forecasts?format=json'

headers = {'x-access-token': 'ENTER_YOUR_KEY'}
parameters = {"latitude": -35.123, "longitude": 149.123, "capacity": 2000}

response = requests.request("GET", url, headers=headers, params=parameters)
data = response.json()

with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

