# Задание 5
earnings = int(input("Введите значение выручки: "))
costs = int(input("Введите значение издержки: "))
margin = earnings - costs
if earnings >= 0 and costs >= 0:
    if margin > 0:
        print("Фирма работает в прибыль")
        profitability = margin / earnings
        print("Рентабельность выручки - ", "%.2f" % profitability)
        employee = int(input("Введите численность сотрудников фирмы: "))
        if employee > 0:
            margin_per_employee = margin / employee
            print("Прибыль фирмы в расчете на одного сотрудника - ", "%.2f" % margin_per_employee)
        else:
            print("Вы ввели недопустимое значение")
    else:
        print("Фирма работает в убыток")
else:
    print("Вы ввели недопустимое значение")
