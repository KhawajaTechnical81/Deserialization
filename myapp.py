import requests
import json

URL = 'http://127.0.0.1:8000/stucreate/'

data = {
    'name': 'Khawaja Moosa',
    'roll': 20,
    'city': 'Sialkot'
}

json_data = json.dumps(data)

r = requests.post(url=URL, data=json_data)

json_data = r.json()

print(json_data)