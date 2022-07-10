"""
    Урок 7. 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31    32         3    5    32        3    5    8    3
37    43         2    4    6         8    3    7    1
51    86        -1   64   -8
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""


def init_matrix(rows, cols):
    return [[0] * cols] * rows


class Matrix:
    def __init__(self, a):
        self.a = a
        self.res = []
        # self.res = init_matrix(len(self.a), len(self.a[0]))

    def __str__(self):
        res = ''
        for row in self.a:
            for col in row:
                res = f'{res} {col}'
            res = f'{res}\n'
        return res

    def __add__(self, other):
        for row in range(len(other.a)):
            self.res.append([])
            for col in range(len(other.a[0])):
                # print(f'self.a[{row}][{col}]+other.a[{row}][{col}] = {self.a[row][col]} + {other.a[row][col]} = {self.a[row][col] + other.a[row][col]}')

                self.res[row].append(self.a[row][col] + other.a[row][col])
                # self.res[row][col] = self.a[row][col] + other.a[row][col]
                # print(f'res[{row}][{col}]: {self.a[row][col] + other.a[row][col]}')

        # return Matrix.map(lambda a, b, **kw: a + b, self, other)
        return Matrix(self.res)


def main():
    # name_lengths = map(len, ['Машаlkkl', 'Петя', 'Вася'])
    # print(*name_lengths)

    # matrix_1 = Matrix([[1, 2, 3], [4, 5, 6]])
    # print(matrix_1, end='', sep=' ')
    #
    # print()

    matrix_2 = Matrix([[11, 2], [14, 9], [94, 3]])
    print(matrix_2, end='', sep=' ')

    print()

    matrix_3 = Matrix([[133, 2], [4, 5], [-93, -100]])
    print(matrix_3, end='', sep=' ')

    print(f'\nsum matrixes:')
    print(matrix_2 + matrix_3, end='', sep='')


if __name__ == '__main__':
    main()
