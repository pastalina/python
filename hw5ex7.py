# Задание 7
import json

profit = {}
average_profit = {}
firms_profit_list = [profit, average_profit]
c = 0
sum_profit = 0
with open("hw5ex7") as firms:
    for line in firms:
        name, form, margin, costs = line.split()
        profit[name] = int(margin) - int(costs)
        if profit.setdefault(name) >= 0:
            sum_profit += profit.setdefault(name)
            c += 1
            average_profit["average_profit"] = sum_profit / c
print(firms_profit_list)

with open("hw5ex7.json", "w") as file:
    json.dump(firms_profit_list, file)