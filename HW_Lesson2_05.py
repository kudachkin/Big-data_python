rating = [9,8,7,6,5,4,3,2,1,9,9,2,3,4]
a = int(input('Введите значение рейтинга - '))
rating.append(a)
rating.sort(reverse=True)
print(rating)
