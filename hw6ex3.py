# Задание 3
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)
        self.wage = wage
        self.bonus = bonus
        print(f"Позиция {self.position}:")

    def get_full_name(self):
        return f"Полное имя: {self.surname} {self.name}"

    def get_total_income(self):
        return f"Доход с учетом премии: {sum(self._income.values())}"


pos = Position("Алина", "Халимова", "Дата-сайентист", 100000, 20000)
print(pos.get_full_name())
print(pos.get_total_income())