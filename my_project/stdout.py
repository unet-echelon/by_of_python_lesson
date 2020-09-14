import subprocess
import requests
# import timedata
from misc import token

url = 'https://api.telegram.org/bot' + token + '/sendmessage?chat_id=-489611067&text='

# r = subprocess.run(['uname', '-a'])
#ip = subprocess.run(['ip', 'addr'])
# print("Пінгую хост...")i

ip = '127.0.0.1'

print()
p = subprocess.run(['ping', '-c', '2', ip], stdout=subprocess.DEVNULL)
if p.returncode == 0:
	text1 = (f"{ip} Хост на зв'язку").format(ip)
	requests.get(url + text1)
else:
	text = (f"{ip} Хост недоступний").format(ip)
	requests.get(url + text)
