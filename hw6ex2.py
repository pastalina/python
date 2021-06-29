# Задание 2
class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width
        self.asphalt_area = _length * _width

    def asphalt_mass(self, mass_per_m2, height):
        self.mass_per_m2 = mass_per_m2
        self.height = height
        return self.asphalt_area * mass_per_m2 * height


r = Road(20, 5000)
r.asphalt_mass(25, 5)
print(
    f"Длина дорожного покрытия: {r._length} м,\n"
    f"Ширина дорожного покрытия: {r._width} м,\n"
    f"Масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см: {r.mass_per_m2} кг/м2*см,\n"
    f"Толщина полотна: {r.height} см.\n"
    f"Масса асфальта, необходимого для покрытия дорожного полотна, равна: {r.asphalt_mass(25, 5)} кг")
