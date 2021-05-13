def my_func(num_1, num_2, num_3):
    return num_1 + num_2 + num_3 - min(num_1, num_2, num_3)

num_1 = float(input('Введите первое число - '))
num_2 = float(input('Введите второе число - '))
num_3 = float(input('Введите третье число - '))

print(my_func(num_1, num_2, num_3))