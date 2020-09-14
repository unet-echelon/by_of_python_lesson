import requests

url = 'https://api.macvendors.com/'
mac = input('mac: ')

def macVendor(mac):
	r = url + mac
	responde = requests.get(r)
	print(responde.text)


macVendor(mac)