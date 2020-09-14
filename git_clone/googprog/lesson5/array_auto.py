auto = [
        'audi',
        'BMW',
        'Mersedes',
        'Fiat',
        'Reno',
        'Ford'
]
print('В нас лише ' + str(len(auto)) + ' авто.')

num = int(input('Введіть номер автомобіля: ')) - 1

if num >= 0 and num <= len(auto):
    print('Ви виграли автомобіль ' + str(auto[num]))
else:
    print('Вибачте машини за вашим номерм не існує')
