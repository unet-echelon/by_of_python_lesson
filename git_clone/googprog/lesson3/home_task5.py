import random

if random.randrange(11) == 10:
	print('Монета встала на ребро')
else:
	if random.randrange(2) == 1:
		print('Выпал орел')
	else:
		print('Выпала решка')