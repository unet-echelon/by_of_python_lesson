def printMax(x,y):
	'''Выводит максимальное из двух чисел.

		Оба занчение должны быть целыми числами.'''
	x = int(x) #Конвернтируєм значине в целие числа
	y = int(y)

	if x > y:
		print(x, 'наибольшое')
	else:
		print(y, 'наибольшое')

printMax(3,5)
print(printMax.__doc__)