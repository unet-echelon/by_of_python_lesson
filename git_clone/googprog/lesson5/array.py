fruts = [
        'apple',
        'orange',
        'banana'
]
print('Корзина містить наступні фрукти: ' + str(fruts))

basket = [] #пустий масив
basket.append('laim')# добавляє лише по одному елементу в масив
basket += ('lemon', 'Cherry', 'Mango')# може добавити список елементів в масив
print(basket)

del basket[1]# видаляє елемент масиву по індексу
basket.remove('Mango')# видаляє елемент масиву за елементом
print(basket)
