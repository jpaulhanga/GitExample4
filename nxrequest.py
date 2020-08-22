import requests
import json


target = "https://10.10.20.58:443/ins"
username = "admin"
password = "Cisco123"


requestsheaders = {"Content-Type": "application/json"}

shcmd = {
  "ins_api": {
    "version": "1.0",
    "type": "cli_show",
    "chunk": "0",
    "sid": "1",
    "input": "sh ip int br",
    "output_format": "json"
  }
}

response = requests.post(
	target,
	data = json.dumps(shcmd),
	headers = requestsheaders,
	auth = (username, password),
	verify = False,
).json()

print(json.dumps(response, indent=2, sort_keys=True))