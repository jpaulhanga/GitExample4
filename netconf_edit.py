from ncclient import manager
from device_detail import router

config_template = open('config_edit.xml').read()

netconf_config = config_template.format(interface_name = "GigabitEthernet2", interface_desc = "Connection to the core router")

with manager.connect(host = router["host"], port = router["port"], username = router["username"], password = router["password"], hostkey_verify=False) as m:
	device_reply = m.edit_config(netconf_config, target = "running")
	m.close_session()
