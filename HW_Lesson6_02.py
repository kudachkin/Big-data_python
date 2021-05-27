class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_area(self):
        area = self._width * self._length
        print(f'Площадь дороги равна {area}')
        thickness = int(input('Введите толщину дороги - '))
        mass = int(input('Введите массу асфальта - '))
        total_area = area * thickness * mass
        print(f'Итого необходимо {total_area} кг асфальта')
        return total_area

calc_length = int(input('Введите длину дороги - '))
calc_width = int(input('Введите ширину дороги - '))

road_1 = Road(calc_length, calc_width)
road_1.calc_area()