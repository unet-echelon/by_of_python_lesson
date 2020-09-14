import time

def shout_and_wait (message):
	print(message)
	time.sleep(1)

shout_and_wait('Поїхали')
shout_and_wait('Перший кілометр')
shout_and_wait('Другий кілометр')
shout_and_wait('Третій кілометр')

print('Приїхали')