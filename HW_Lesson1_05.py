revenue = int(input("Введите объем выручки - "))
costs = int(input("Введите сумму издержек - "))
if revenue > costs:
    income = revenue - costs
    RET = revenue / costs
    print("Фирма получила прибыль")
    print("Прибыль равна", income)
    print("Рентабельность равна", RET)
    staff = int(input("Введите количество сотрудников фирмы - "))
    RET_staff = income / staff
    print("Рентабельность в расчете на сотрудника равна", RET_staff)

else:
    loss = costs - revenue
    print("Фирма получила убыток")
    print("Убыток составил", loss)