# Задание 4-6
class Warehouse:
    def __init__(self):
        self.nomenclature = []
        self.department_machines = {}
        self.department = ""

    def accept(self, *machines):
        for machine in machines:
            self.nomenclature.append(machine)

    def transfer(self, department, *machines):
        self.department = department
        self.department_machines = {department: (machine for machine in machines)}

    def __str__(self):
        return f'На складе: {self.nomenclature}, в {self.department} находятся {self.department_machines.get("IT")}'


class Machines:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
        self.position = {name: quantity}

    def str(self):
        return f"{self.name} в количестве {self.quantity} шт."

    def my_list(self):
        return self.position


class Printer(Machines):
    def __init__(self, quantity):
        name = "принтер"
        super().__init__(name, quantity)


class Scanner(Machines):
    def __init__(self, quantity):
        name = "сканнер"
        super().__init__(name, quantity)


class Copier(Machines):
    def __init__(self, quantity):
        name = "ксерокс"
        super().__init__(name, quantity)


p1 = Printer(4)
p2 = Printer(2)
print(p1.position)
print(p2.position)
s1 = Scanner(2)
c1 = Copier(5)
print(s1.position)
print(c1.position)
w = Warehouse()
w.accept(p1, p2, s1, c1)
print(w.nomenclature[0].my_list(), w.nomenclature[1].my_list(),
      w.nomenclature[2].my_list(), w.nomenclature[3].my_list())
w.transfer("IT", p1, s1)
print(w.department_machines.get("IT"))
print(w)
