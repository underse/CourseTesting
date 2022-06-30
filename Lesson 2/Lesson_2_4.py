"""
Урок 2. 4.
"""


def print_header(num):
    print()
    print(f'{"=" * 20} Упражнение № {num} {"=" * 20}')


def task_4():
    print_header(4)
    my_str = input('Введите строку разделённую пробелами: ')
    i = 1
    for word in my_str.split(' '):
        print(f'{i:5d}\t{word:.10}')
        i += 1


def main():
    task_4()


if __name__ == '__main__':
    main()
