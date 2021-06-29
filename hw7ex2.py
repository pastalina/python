# Задание 2
from abc import ABC, abstractmethod

class AbstractClothes(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def fabric_calc(self):
        pass


class Clothes(AbstractClothes):
    def __init__(self, param):
        self.param = param
        self.category = "category"
        self.fabric = 0

    @property
    def fabric_calc(self):
        return f"Вид изделия: {self.category}. Расход ткани составляет: {self.fabric} м"

    def __add__(self, other):
        return f"Общий расход ткани составит: {self.fabric + other.fabric} м"


class Coat(Clothes):
    def __init__(self, param):
        super().__init__(param)
        self.category = "пальто"

    @property
    def fabric_calc(self):
        self.fabric = round(self.param / 6.5 + 0.5, 2)
        return f"Вид изделия: {self.category}. Расход ткани составляет: {self.fabric} м"


class Suit(Clothes):
    def __init__(self, param):
        super().__init__(param)
        self.category = "костюм"

    @property
    def fabric_calc(self):
        self.fabric = round(2 * self.param + 0.3, 2)
        return f"Вид изделия: {self.category}. Расход ткани составляет: {self.fabric} м"


c = Coat(42)
s = Suit(1.7)
print(c.fabric_calc)
print(s.fabric_calc)
print(c + s)