"""
5. Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти чётные числа от 100 до 1000 (включая границы). Нужно получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""
from functools import reduce


def multiply(prev_el, el):
    return prev_el * el


def main():
    new_list = [el for el in range(100, 1000+1) if el % 2 == 0]
    print(f'Чётные числа в диапазоне 100..1000: {new_list}')

    print(reduce(multiply, new_list))


if __name__ == '__main__':
    main()
