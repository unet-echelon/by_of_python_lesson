def total(a=5, *numbers, **phonebook):
	print('a', a)
	#Проход по всем елементам кортежа
	for single_items in numbers:
		print('single_items', single_items)

	#Проход по всем елементам словаря
	for first_part, second_part in phonebook.items():
		print(first_part,second_part)
print(total(10,1,2,3,Jack=1122,John=2231,Inge=1560))