import sys

def sklonenie (number2, krokodil, krokodila, krokodilov):

    ostatok = number % 10

    if (ostatok == 1):
        return krokodil
    elif (ostatok >= 2 and ostatok <= 4):
        return krokodila
    else: #(ostatok == 5 and ostatok == 0):
        return krokodilov

# number2 = sys.argv[1]

number = int(input(' Enter: '))

print(str(number))
print(sklonenie(number , " негритёнок", " Негритёнка", " Негритят"))
