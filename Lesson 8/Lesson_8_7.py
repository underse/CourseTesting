"""
     Урок 8. 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
     Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта.
     Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
     Проверьте корректность полученного результата.
"""
import cmath


class Complex:
    def __init__(self, c):
        self.c = c
        print(f'Создано комплексное число: {self.c}')

    def __add__(self, other):
        res = self.c + other.c
        print(f'Сложение комплексных чисел {self.c} + {other.c} = {res}')
        return res

    def __mul__(self, other):
        res = self.c * other.c
        print(f'Умножение комплексных чисел {self.c} * {other.c} = {res}')
        return res


def main():
    c1 = Complex(9 + 4j)
    c2 = Complex(15 + 8j)

    print(c1 + c2)
    print(c1 * c2)

    print(f'\nПроверка комплексных чисел через модуль cmath')
    cmath1 = complex(9, 4)
    cmath2 = complex(15, 8)
    print(f'complex(9, 4) + complex(15, 8) = {cmath1 + cmath2}')
    print(f'complex(9, 4) * complex(15, 8) = {cmath1 * cmath2}')


if __name__ == '__main__':
    main()
