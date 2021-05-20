from itertools import count, cycle

for el in count(3):
    el = int(el)
    if el == 10:
        break
    else:
        print(el)

a = 0
for el2 in cycle("XYZ"):
    if a > 10:
        break
    print(el2)
    a += 1