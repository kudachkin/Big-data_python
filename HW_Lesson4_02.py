from functools import reduce
my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
i = 1
i += 1
list_new = [el for el in my_list if int(my_list[i]) > int(my_list[i - 1])]
print(list_new)