import random
print(" Гра має імя - Камінь, Ножниці, Папір" \
"Приві, гравцю, давай познайомимось.\n \
Як тебе звати")
name = input(' ')
print(' Дуже приємно ' + name)
###Початок гри
games_array = ['Камінь', 'Ножниці', 'Бумага']
print(' Умови гри: Камінь ломає ножниці, Папір - накриває камінь,\n Ножниці - ріжуть папір\n \
Потрібно вибрати щось одне\n \
0 - Камінь\n \
1 - Ножниці\n \
2 - Папір')
#вибір елементу
users = int(input(' '))
comp = random.randrange(3) - 1

if users > len(games_array):
    exit(name + ' Ви ввели невірне число.')
elif users == comp:
    exit(' Нічия' + ' ПК вибрав ' + str(comp) + ' Користувач вибрав ' + str(users))

if users == 0 and comp == 1:
    print(name + ' вибрав ' + str(users) + ' і виграв.' + 'ПК вибрав ' + str(comp) + ' і програв.')
elif users == 0 and comp == 2:
    print('ПК вибрав ' + str(comp) + ' і виграв, ' + str(name) + ' вибрав ' + str(users) + ' і  програв')

if users == 1 and comp == 0:
    print('ПК вибрав ' + str(comp) + ' і виграв, ' + str(name) + ' вибрав ' + str(users) + ' і  програв')
elif users == 1 and comp == 2:
    print(name + ' вибрав ' + str(users) + ' і виграв.' + 'ПК вибрав ' + str(comp) + ' і програв.')

if users == 2 and comp == 0:
    print(name + ' вибрав ' + str(users) + ' і виграв.' + 'ПК вибрав ' + str(comp) + ' і програв.')
elif users == 2 and comp == 1:
    print(name + ' вибрав ' + str(users) + ' і виграв.' + 'ПК вибрав ' + str(comp) + ' і програв.')
