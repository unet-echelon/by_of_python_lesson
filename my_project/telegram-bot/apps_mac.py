#import config
import requests
import json
from time import sleep


token = "token"
URL = 'https://api.telegram.org/bot' + token + '/'

global last_update_id
last_update_id = 0

def get_updates():
    url = URL + 'getupdates'
    r = requests.get(url)
    return r.json()


def get_massage():

	data = get_updates()
	last_objeck = data['result'][-1]
	current_udate_id = last_objeck['update_id']

	global last_update_id
	if last_update_id != current_udate_id:
		last_update_id = current_udate_id

		chat_id = last_objeck['message']['chat']['id']
		message_text = last_objeck['message']['text']

		message = {'chat_id': chat_id,
				   'text': message_text}
		return message
	return None

def sent_massage(chat_id, text='Not Found'):
	url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
	requests.get(url)

#API Mac Vendor
url_mac = 'https://api.macvendors.com/'
def macVendor(text="Not Found"):
    r = url_mac + text
    responde = requests.get(r)
    return(str(responde.text))

def macaddr(text):
	test = str(text.replace(':.-', ''))
	# test1 = str(text.replace('.',''))
	# test2 = str(text.replace('-',''))
	return test

def main():
	while True:
		answer = get_massage()
		if answer != None:
			chat_id = answer['chat_id']
			text = answer['text']
			sent_massage(chat_id, macaddr(text))
		else:
			continue
		sleep(10)




if __name__ == '__main__':
	main()