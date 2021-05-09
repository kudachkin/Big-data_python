list = ['winter', 'spring', 'summer', 'autumn']
month = int(input('Введите целое число от 1 до 12 - '))
if month > 12:
    print('Число больше 12, ввод не принят')
elif month <= 2 or month == 12:
    print(list[0])
elif month <= 5:
    print(list[1])
elif month <= 8:
    print(list[2])
else:
    print(list[3])




#else:

#my_dict = {'winter': 1, 'spring': 4, 'summer': 7, 'autumn': 10}
#print(my_dict.values())
