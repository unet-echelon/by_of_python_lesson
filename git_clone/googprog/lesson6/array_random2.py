import random
lenght = int(input('Якої довжини потрібен масив: '))
array = []
index = 0
while index < lenght:
	array.append(random.randrange(100))
	index += 1

print(array)
print(max(array))
max_val = 0
for item in array:
	if item > max_val:
		max_val = item
print(str(max_val))