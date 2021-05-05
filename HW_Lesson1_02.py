sec_input = int(input("Введите количество секунд - "))
hours = int(sec_input // 3600)
print(hours)
a = sec_input % 3600
print(a)
minutes = a // 60
print(minutes)
seconds = a % 60
print(seconds)
print(hours,"час(ов):",minutes,"минут:",seconds,"секунд")