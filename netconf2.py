from ncclient import manager
import xmltodict
from pprint import pprint
from device_detail import router


netconf_filter = open('netfilter.xml').read()

with manager.connect(host = router["host"], port = router["port"], username = router["username"], password = router["password"], hostkey_verify = False) as m:
	for capability in m.server_capabilities:
		print('*' * 50)
		print(capability)

		print("connected")

		interface_netconf = m.get(netconf_filter)
		interface_python = xmltodict.parse(interface_netconf.xml) ["rpc-reply"]["data"]

		pprint(interface_python)

		name = interface_python['interfaces']['interface']['name']['#text']

		print(name)

		config = interface_python["interfaces"]["interface"]
		op_state = interface_python["interfaces-state"]["interfaces"]

		print("start")
		print(f"name: {config['name']['#text']}")
		print(f"Description:{config['description']}")
		print(f"Packet_In:{op_state['statistics']['in-unicast-pkts']}")




	m.close_session()