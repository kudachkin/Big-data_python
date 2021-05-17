old_list = [2, 2, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10, 10, 10]

new_list = [el for el in old_list if old_list.count(el) == 1]
print(new_list)