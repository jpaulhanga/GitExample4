import requests
from pprint import pprint

url = "https://10.10.20.58/api/aaalogin.json"

payload = "{\n\t\"aaalogin\": {\n\t\t\"attributes\": {\n\t\t\t\"name\": \"admin\",\n\t\t\t\"pwd\": \"Cisco123\"\n\t\t}\n\t}\n}"
headers = {
  'Content-Type': 'application/json'
}

response = requests.post(url, headers=headers, data = payload, verify=False).json()
token = response['imdata'][0]['aaalogin']['attributes']['token']

#pprint(response)
print(token)


url = "https://10.10.20.58/api/node/class/l2BD."

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))

