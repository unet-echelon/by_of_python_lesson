array =[]
number = int(input('Введіть число: '))
item = 1
while item <= number:
	array.append(item)
	item += 1

print(str(array))
print(str(sum(array)))