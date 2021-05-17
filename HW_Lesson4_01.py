import my_scripts

rate = int(input('Введите ставку сотрудника - '))
hours = int(input('Введите выработку в часах сотрудника - '))
premium = int(input('Введите размер премии сотрудника - '))

salary = my_scripts.salary_calc(rate, hours, premium)
print(salary)