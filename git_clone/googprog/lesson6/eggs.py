eggs = [0, 5, 5, 0, 0, 0, 5, 0, 8, 8, 8, 0, 5, 0, 6]

good_eggs = []

broken_eggs = 0
for item in eggs:
    if item != 0:
        broken_eggs += 1
    else:
        good_eggs.append(item)

print('Всі яйця ' + str(len(eggs)))
print('Хороші яйця ' + str(len(good_eggs)))
print('Погані яйця ' + str(broken_eggs))
