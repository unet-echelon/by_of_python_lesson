from conf import login
from conf import password
import smtplib
from imaplib import IMAP4_SSL

server = "mail.uar.net"

# HOST = "imap.yandex.ru"
# PORT = 993
USER = "LOGIN"
PASSWORD = "PASSWROD"
# SENDER = "Yoba"

connection = IMAP4_SSL(host=server)
connection.login(user=login, password=password)
status, msgs = connection.select('INBOX')
assert status == 'OK'

typ, data = connection.search(None, 'FROM', '"%s"', "Forwarded")
print(data)
for num in data[0].split():
    typ, message_data= connection.fetch(num, '(RFC822)')
    print(data)
    print('Message %s\n%s\n' % (num, message_data[0][1]))
connection.close()
connection.logout()
