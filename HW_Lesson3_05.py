my_list = input('Введите несколько чисел через пробел - ')
new_list = [int(i) for i in my_list.split()]

def sum_func(new_list):
    new_list = sum(new_list)
    return new_list

print(sum_func(new_list))
