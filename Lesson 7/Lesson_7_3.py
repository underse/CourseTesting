"""
    Урок 7. 3. Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка.
    В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
    В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
    Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
Умножение. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
Деление. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.

В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернёт строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернёт строку: *****\n*****\n*****.
Подсказка: подробный список операторов для перегрузки доступен по ссылке.

Дополнительные материалы
Перегрузка операторов
"""
import sys


class Cell:
    def __init__(self, count):
        try:
            self.count = int(count)
            print(f'Создан класс {self.__class__.__name__} c {self.count} клетками.')
        except TypeError as e:
            print('Число клеток должно быть целым числом!')
            sys.exit(-1)

    def __add__(self, other):
        return Cell(self.count + other.count)
        # return self.count + other.count

    def __sub__(self, other):
        print(f'Вычитание: Cell({self.count}) - Cell({other.count})')
        if self.count - other.count < 0:
            raise ValueError('!Вычитание невозможно. Разница меньше 0.')
        return Cell(self.count - other.count)

    def __mul__(self, other):
        return Cell(self.count * other.count)
        # return self.count * other.count

    def __floordiv__(self, other):
        return Cell(self.count // other.count)
        # return self.count // other.count

    def make_order(self, cr):
        print(f'\n{self.__class__.__name__}, количество ячеек в ряду: {cr}')
        c = self.count // cr
        remainder = self.count % cr
        s = ''
        print(c, remainder)
        for i in range(c):
            s = f'{s}\n{("*" * cr)}'
        if remainder > 0:
            s = f'{s}\n{("*" * remainder)}'
        return s


def main():
    cell_1 = Cell(45)

    cell_2 = Cell(17)

    print(f'\nСложение: Cell({cell_1.count}) + Cell({cell_2.count}) = {(cell_1 + cell_2).count}\n')
    try:
        print(f'Вычитание: Cell({cell_1.count}) - Cell({cell_2.count}) = {(cell_1 - cell_2).count}')
    except ValueError as err:
        print(err)

    try:
        print(f'\nВычитание: Cell({cell_2.count}) - Cell({cell_1.count}) = {(cell_2 - cell_1).count}')
    except ValueError as err:
        print(err)
    print(f'\nУмножение: Cell({cell_1.count}) * Cell({cell_2.count}) = {(cell_1 * cell_2).count}')

    print(f'\nДеление: Cell({cell_1.count}) // Cell({cell_2.count}) = {(cell_1 // cell_2).count}')

    print(f'{cell_1.make_order(9)}')
    print(f'{cell_1.make_order(8)}')


if __name__ == '__main__':
    main()
