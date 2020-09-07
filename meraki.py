import requests
import json

url = "https://dashboard.meraki.com/api/v0/organiations"

headers = {
  'x-cisco-api': '7b750b19efea8ee6d0949de5783d99359dc1a381'
}

response = requests.get(url, headers=headers).json()

print(json.dumps(response, indent=2, sort_keys=True))
for response_org in response:
	if response_org['name'] == 'Devnet Sandbox':
		orgid = response_org['id']

print(orgid)

