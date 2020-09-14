def vidminuvanna (num, hryvnia, hryvni, hryven):
    ostatok = num % 10

    if (ostatok == 1):
        return hryvnia
    elif (ostatok >= 2 and ostatok <= 4):
        return hryvni
    else: # (ostatok >= 5 and ostatok == 0):
        return hryven

num = int(input('Введить сумму: '))

print(str(num) + vidminuvanna(num, ' гривня',' гривні',' гривень') )
