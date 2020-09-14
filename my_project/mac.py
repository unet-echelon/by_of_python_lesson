#!bin/bash env python3
from colorama import init
from colorama import Fore, Back, Style
import requests
init()

print( Fore.GREEN )
print(' Convert MAC-addresses')
print()
print( Fore.CYAN)

while True:
    def macDash(mac):
        remv1 = macnew[:2]
        remv2 = macnew[2:4]
        remv3 = macnew[4:6]
        remv4 = macnew[6:8]
        remv5 = macnew[8:10]
        remv6 = macnew[10:12]
        print(' Done: ' + (remv1 + '-' + remv2 + '-' + remv3 + '-' + remv4 + '-' + remv5 + '-' + remv6).upper())

    def macPoint(mac):
        remv1 = macnew[:4]
        remv2 = macnew[4:8]
        remv3 = macnew[8:]
        print(' Done: ' + (remv1 + '.' + remv2 + '.' + remv3).lower())

    def macTwoDots(mac):
        remv1 = macnew[:2]
        remv2 = macnew[2:4]
        remv3 = macnew[4:6]
        remv4 = macnew[6:8]
        remv5 = macnew[8:10]
        remv6 = macnew[10:12]
        print(' Done: ' + (remv1 + ':' + remv2 + ':' + remv3 + ':' + remv4 + ':' + remv5 + ':' + remv6).upper())

    def macTwoDots_lower(mac):
        remv1 = macnew[:2]
        remv2 = macnew[2:4]
        remv3 = macnew[4:6]
        remv4 = macnew[6:8]
        remv5 = macnew[8:10]
        remv6 = macnew[10:12]
        print(' Done: ' + (remv1 + ':' + remv2 + ':' + remv3 + ':' + remv4 + ':' + remv5 + ':' + remv6).lower())

    def macVendor(mac):
        r = url + mac
        responde = requests.get(r)
        print(' Vendor: ' + responde.text)


    url = 'https://api.macvendors.com/'
    mac = input(' Enter the MAC address: ').strip()
    if mac == 'quit':
        exit('Close')
    elif len(mac) != 17 and len(mac) != 14 and len(mac) != 12:
        exit('Close')
    else:
        for item in mac:
            if item == '-':
                macnew = mac.replace('-', '')
                break
            elif item == ':':
                macnew = mac.replace(':', '')
                break
            elif item == '.':
                macnew = mac.replace('.','')
                break
            else:
                macnew = mac

    print()
    macDash(mac)
    macTwoDots(mac)
    macTwoDots_lower(mac)
    macPoint(mac)
    macVendor(mac)
    print()
