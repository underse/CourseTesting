"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника. Используйте в нём формулу: (выработка в часах*ставка в час) + премия. Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.
"""
import sys
from sys import argv
from time import sleep


def calc_salary(hours, rate, bonus):
    return (hours*rate) + bonus


def main():
    script_name = ''
    try:
        # hours, rate, bonue = map(float, argv[1:]
        script_name, hours, rate, bonus = argv
    except IndexError as e:
        print('Запуск с параметрами:')
        print(f'{script_name} hours rate_per_hour bonus')
        sys.exit(-1)
    except ValueError as e:
        print('Запуск с параметрами:')
        print(f'{script_name} hours rate_per_hour bonus')
        sys.exit(-1)

    try:
        hours = float(hours)
        rate = float(rate)
        bonus = float(bonus)
    except ValueError as e:
        print('Проверьте введёные данные. Должны быть только цифры.')
        sys.exit(-1)

    print(f'Выработка в часах: {hours:.2f}')
    print(f'ставка в час: {rate:.2f}')
    print(f'Премия: {bonus:.2f}')

    print(f'\nИтого, заработная плата: {calc_salary(hours, rate, bonus):.2f} у.е.')


if __name__ == '__main__':
    main()
