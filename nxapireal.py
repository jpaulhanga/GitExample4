##NX-API CLI##
import requests
import json

"""
Modify these please
"""
url='https://10.10.20.58/ins'
switchuser='admin'
switchpassword='Cisco123'

myheaders={'content-type':'application/json'}
payload={
  "ins_api": {
    "version": "1.0",
    "type": "cli_show",
    "chunk": "0",
    "sid": "1",
    "input": "sh cd nei",
    "output_format": "json"
  }
}
response = requests.post(
			url,
			data=json.dumps(payload), 
			headers=myheaders,
			auth=(switchuser,switchpassword), 
			verify=False).json()

##print(json.dumps(response, indent = 2, sort_keys=True))

##NX-API REST###
##creating a token##
auth_url = 'https://10.10.20.58:443/api/aaaUser.json'
auth_body = {"aaaUser": {"attributes": {"name": "switchuser", "pwd": "switchpassword"}}}
auth_response = requests.post(auth_url, data = json.dumps(auth_body), timeout = 5, verify=False).json()
#token = auth_response['imdata'][0]['aaaUser']['attributes']['token']
#cookies = {}
#cookies['APIC-cookie'] = token

counter = 0
nei_count = response['ins_api']['outputs']['output']['body']['neigh_count']

while counter < nei_count:
	hostname = response['ins_api']['outputs']['output']['body']['TABLE_cdp_neighbor_brief_info']['ROW_cdp_neighbor_brief_info'][counter]['device_id']
	local_int=response['ins_api']['outputs']['output']['body']['TABLE_cdp_neighbor_brief_info']['ROW_cdp_neighbor_brief_info'][counter]['intf_id']
	remote_int=response['ins_api']['outputs']['output']['body']['TABLE_cdp_neighbor_brief_info']['ROW_cdp_neighbor_brief_info'][counter]['port_id']

	body = {
		"l1phyif": {
			"attributes": {
				"descr": connected to +'hostname'+ remote if is +'remote_int'
			}
		}
	}

	counter += 1
