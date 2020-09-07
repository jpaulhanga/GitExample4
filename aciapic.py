import requests
import json
from pprint import pprint

url = "https://10.10.20.14:443/api/aaaLogin.json"

payload = {
    "aaaUser": {
        "attributes": {
            "name": "admin",
            "pwd": "C1sco12345"
        }
    }
}

headers = {
  'Content-Type': 'application/json'}

response = requests.post(url, headers=headers, data =json.dumps(
    payload), verify=False).json()

##print(json.dumps(response, indent=2, sort_keys=True))

token  = response['imdata'][0]['aaaLogin']['attributes']['token']
cookie ={}
cookie['APIC-Cookie'] = token
print(token)