"""
    Урок 7. 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
    Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
    К типам одежды в этом проекте относятся пальто и костюм.
    У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
    Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""

from abc import ABC, abstractmethod


class Clothing(ABC):
    def __init__(self, name=''):
        self.name = name
        self.sum_consumption = 0

    @abstractmethod
    def fabric_consumption(self):
        pass


class Suit(Clothing):
    def __init__(self, name, size):
        self.size = size
        super().__init__(name)

    @property
    def fabric_consumption(self):
        return self.size / 6.5 + 0.5


class Coat(Clothing):
    def __init__(self, name, height):
        self.height = height / 100
        super().__init__(name)

    @property
    def fabric_consumption(self):
        return 2 * self.height + 0.3


def main():
    suit_1 = Suit('Пальто кашемировое', 50)
    # print(suit_1)
    print(suit_1.name, suit_1.size)
    print(f'Расход ткани на: {suit_1.name}, {suit_1.size} размера - {suit_1.fabric_consumption:.2f} метров.')

    print()

    coat = Coat('Костюм мужской с отливом', 188)
    # print(coat)
    print(coat.name, coat.height)
    print(f'Расход ткани на: {coat.name}, {coat.height} роста - {coat.fabric_consumption:.2f} метров.')

    print(f'\nОбщий расход ткани: {(suit_1.fabric_consumption + coat.fabric_consumption):.2f} метров')


if __name__ == '__main__':
    main()
