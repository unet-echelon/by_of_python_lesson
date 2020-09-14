import sys

print('Аргументы командной строки: ')
for i in sys.argv:
	print(i)
print('\nПеременная PYTHONPATH содержыт', sys.path, '\n')