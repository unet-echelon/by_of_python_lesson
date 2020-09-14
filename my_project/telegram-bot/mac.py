import requests

url = 'https://api.macvendors.com/'
text = mac   
def macVendor(mac):
    r = url + mac
    responde = requests.get(r)
    return(str(responde.text))
