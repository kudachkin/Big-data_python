from functools import reduce
n = input('Введите число - ')

my_list = [el for el in range(1, int(n) + 1)]
fact = reduce(lambda x, y: x * y, my_list)
print(my_list)
print(fact)