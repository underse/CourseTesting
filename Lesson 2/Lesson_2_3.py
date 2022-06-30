"""
Урок 2. 3.
"""


def print_header(num):
    print()
    print(f'{"=" * 20} Упражнение № {num} {"=" * 20}')


def task_3():
    print_header(3)
    month = int(input('Введите значение месяца в виде целого числа от 1 до 12: '))

    year = {'зима': [1, 2, 12], 'весна': [3, 4, 5], 'лето': [6, 7, 8], 'осень': [9, 10, 11]}
    for key, value in year.items():
        if month in value:
            print(f'Месяц № {month} относится ко времени года: {key}.')


def main():
    task_3()


if __name__ == '__main__':
    main()
