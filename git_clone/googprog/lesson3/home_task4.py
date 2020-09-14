from datetime import *

x = datetime.now()
print(x)
y = datetime.now().weekday()
print("Номер дня", y)
if y == 0 and y == 6:
	print('Выходной')
else:
	print('Сегодня будний день, за роботу')