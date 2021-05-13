def my_mult (x, y):
    return x ** y

x = abs(float(input('Введите число x - ')))
y = round(float(input('Введите число y - ')))

if y > 0:
    y = 0 - y
else:
    y = y

print(my_mult(x, y))