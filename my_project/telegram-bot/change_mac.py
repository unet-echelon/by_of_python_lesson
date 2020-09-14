#!bin/bash env python3
from apps_mac import get_massage


while True:
    def macDash(text):
        remv1 = macnew[:2]
        remv2 = macnew[2:4]
        remv3 = macnew[4:6]
        remv4 = macnew[6:8]
        remv5 = macnew[8:10]
        remv6 = macnew[10:12]
        print(' Done: ' + (remv1 + '-' + remv2 + '-' + remv3 + '-' + remv4 + '-' + remv5 + '-' + remv6).upper())

    def macPoint(text):
        remv1 = macnew[:4]
        remv2 = macnew[4:8]
        remv3 = macnew[8:]
        print(' Done: ' + (remv1 + '.' + remv2 + '.' + remv3).lower())

    def macTwoDots(text):
        remv1 = macnew[:2]
        remv2 = macnew[2:4]
        remv3 = macnew[4:6]
        remv4 = macnew[6:8]
        remv5 = macnew[8:10]
        remv6 = macnew[10:12]
        print(' Done: ' + (remv1 + ':' + remv2 + ':' + remv3 + ':' + remv4 + ':' + remv5 + ':' + remv6).upper())

    def macTwoDots_lower(text):
        remv1 = macnew[:2]
        remv2 = macnew[2:4]
        remv3 = macnew[4:6]
        remv4 = macnew[6:8]
        remv5 = macnew[8:10]
        remv6 = macnew[10:12]
        print(' Done: ' + (remv1 + ':' + remv2 + ':' + remv3 + ':' + remv4 + ':' + remv5 + ':' + remv6).lower())

for item in text:
    if item == '-':
        macnew = text.replace('-', '')
        break
    elif item == ':':
        macnew = text.replace(':', '')
        break
    elif item == '.':
        macnew = text.replace('.','')
        break
    else:
        macnew = text

    # print()
    macDash(mac)
    # macTwoDots(mac)
    # macTwoDots_lower(mac)
    # macPoint(mac)
    # macVendor(mac)
    # print()
