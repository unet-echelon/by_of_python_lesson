import random
import math
rand = random.randrange(15)
number = int(input('Введите число от 0 до 15: '))
if rand == number:
	print('Ура, Вы угадалчи сисло')
elif rand < number:
	print('Секретное число меньше указаного')
elif rand > number:
	print('Секретное число больше указаного')
if abs((rand - number) < 3):
	print('Тепло')
else:
	print('Холодно')
number = int(input('Введите число от 0 до 15: '))
if rand == number:
	print('Ура, Вы угадалчи сисло')
elif rand < number:
	print('Секретное число меньше указаного')
elif rand > number:
	print('Секретное число больше указаного')
if abs((rand - number) < 3):
	print('Тепло')
else:
	print('Холодно')
number = int(input('Введите число от 0 до 15: '))
if rand == number:
	print('Ура, Вы угадалчи сисло')
elif rand < number:
	print('Секретное число меньше указаного')
elif rand > number:
	print('Секретное число больше указаного')
if abs((rand - number) < 3):
	print('Тепло')
else:
	print('Холодно')
print('Вы не угадали число, Секретное число: ', rand)