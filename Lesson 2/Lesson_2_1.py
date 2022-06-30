"""
Урок 2. 1.
"""


def print_header(num):
    print()
    print(f'{"=" * 20} Упражнение № {num} {"=" * 20}')


def task_1():
    print_header(1)
    my_list1 = [1, 'abc', {'key1': 123, 'key99': 99999}, True, False, (2, 6, 10)]
    for el in my_list1:
        print(type(el))


def main():
    task_1()


if __name__ == '__main__':
    main()
