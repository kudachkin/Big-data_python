def my_divide (num_1, num_2):
    return num_1 / num_2

num_1 = float(input('Введите делимое - '))
num_2 = float(input('Введите делитель - '))

if num_2 == 0:
    print('Делить на 0 нельзя, конец программы')

else:
    print(my_divide(num_1, num_2))
