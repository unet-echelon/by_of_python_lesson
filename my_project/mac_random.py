import random

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "a", "b", "c", "d", "e", "f",]
mac = ''

for i in range(12):
    mac = str(mac) + str(random.choice(a))

print(mac)
