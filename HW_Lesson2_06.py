text = input('Введите наименование товаров через пробел - ')
print(text)
items = list(text.split())

for i in range(int(len(items))):
    price = input(f'Введите цену товара {items[i]} - ')
    quant = input(f'Введите количество товара {items[i]} - ')
    value = input(f'Введите единицу измерения {items[i]} - ')
    data = {'Наименование': (items[i]), 'Цена': (price), 'Количество': (quant), 'Ед измерения': (value)}
    print(data)
