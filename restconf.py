import requests
import json
from pprint import pprint

#set connection parameters in a dictionary
router = {"host": "Cisco-IOS-XE", "port": "443", 
		  "username": "developer", "password": "C1sco12345"}

#set restconf API headers
headers = {"Action":"application/yang-data+json",
		   "Content-Type": "application/yang-data+json"}

url = {f"https://{router['host']}:{router['port']}/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces/interface=GigabitEthernet1"}

response = requests.get(url, headers=headers, auth=(
	router['username'], router['password']), verify=False)

api_data = response.json
print("/" * 50)
pprint(api_data["Cisco-IOS-XE-interfaces-oper:interfaces"]["description"])
if api_data["Cisco-IOS-XE-interfaces-oper:interface"]["admin-status"] == 'if-status-up':
	print("Interface is up")


