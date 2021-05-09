text = input('Введите несколько слов - ')
print(text)
my_list = list(text.split())
print(my_list)
for i in my_list:
    a = int(my_list.index(i) + 1)
    print(a, i[0:10])
