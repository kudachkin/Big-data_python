text = input('Введите несколько слов - ')
print(text)
my_list = list(text.split())
print(my_list)
print(len(my_list))

a = 0
for i in range(int(len(my_list)/2)):
    my_list[a], my_list[a+1] = my_list[a+1], my_list[a]
    a += 2

print(my_list)
