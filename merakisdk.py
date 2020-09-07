from meraki_sdk.meraki_sdk_client import MerakiSdkClient
import json
from pprint import pprint

token = "7b750b19efea8ee6d0949de5783d99359dc1a381"
meraki  = MerakiSdkClient(token)

orgs = meraki.organizations.get_organizations()
pprint (orgs)

for orgName in orgs:
	if orgName['name'] == 'DevNet Sandbox':
		orgid = orgName['id']
print(orgid)




