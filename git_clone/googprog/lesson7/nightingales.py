import sys
import math

# temper = sys.argv[1]
temper = None
if temper == None:
    temper = int(input('Введіть температуру: '))
else:
    temper = int(temper)


# season = sys.argv[0]
season = None
if season == None:
    season = int(input('Яка у вас пора року (0 - весна, 1 - літо, 2 - осінь, 3 - зима)'))
else:
    season = int(season)

if (15 <= temper <= 35):
    print('Скорее идите в парк, соловьи поют!')
elif (22 <= temper <= 30):
    print('поют в любое время года')
elif (temper <= 14):
    print('Слишком холодно, соловьи в теплых краях')
elif (temper >= 35):
    print('Слишком жарко что бы пели соловьи')

# if temper >= 15 and temper <= 35:
#     print('Скорее идите в парк, соловьи поют!')
# elif temper >= 22 and temper <= 30:
#     print('поют в любое время года')
# elif temper <= 14:
#     print('Слишком холодно, соловьи в теплых краях')
# elif temper >= 35:
#     print('Слишком жарко что бы пели соловьи')
