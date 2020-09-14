import time

name = []
username = None
while username != 'Еліс':
	username = input('Введіть свое ім"я: ').capitalize()
	name.append(username)

for item in name:
	print('З нами ' + item)
	time.sleep(1)
	if item == 'Еліс':
		print('Еліс?? Хто така Еліс?')
		break
time.sleep(2)
print('Що це за дівчина і де вона проживає?')
time.sleep(1)
print('А вдруг вона не курить? А можливо вона не п"є?')
time.sleep(1)
print('А ми з такими мордами візьмемо і прийдемо до Еліс.')
time.sleep(1)



print(str(name))