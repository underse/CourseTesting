"""
    Урок 6. 2. Реализовать класс Road (дорога).
определить атрибуты: length (длина), width (ширина);
значения атрибутов должны передаваться при создании экземпляра класса;
атрибуты сделать защищёнными;
определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см*число см толщины полотна;
проверить работу метода.
Например: 20 м*5000 м*25 кг*5 см = 12500 т.
"""


class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc(self, mass, thickness):
        return self._length * self._width * mass * thickness


def main():
    length = 200
    width = 15

    mass = 40
    thickness = 5
    road = Road(length, width)
    res = road.calc(mass=mass, thickness=thickness)
    print(
        f'Для покрытия дороги длиной {length} и шириной {width} м. при {mass} кг/кв.метр толщиной {thickness} см., необходимо {res} кг асфальта.')


if __name__ == '__main__':
    main()
