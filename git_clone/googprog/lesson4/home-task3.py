#Конвертор валют
print("Какая у вас на руках валюта? \n1. Гривны \n2. Долары")
money = int(input('Выберите валюту 1 или 2: '))
if money == 1:
	usd = float(input('Введите цену 1 доллара: '))
	uah = float(input('Сколькок у вас гривен: '))
	ball = uah / usd
	print("Сумма в долларах ", format(ball, '.2f'))
elif money == 2:
	usd = float(input('Введите цену 1 доллара: '))
	uah = float(input('Сколькок у вас долларов: '))
	ball = usd * uah
	print("Сумма в гривнах ", format(ball, '.2f'))