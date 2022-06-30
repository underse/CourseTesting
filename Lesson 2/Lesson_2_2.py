"""
Урок 2. 2.
"""


def print_header(num):
    print()
    print(f'{"=" * 20} Упражнение № {num} {"=" * 20}')


def task_2():
    print_header(2)
    my_list = input('Введите элементы списка разделённые одним пробелом: ').split(' ')
    print(my_list)

    # обработка чётности/нечётности
    if len(my_list) % 2 == 0:
        r = len(my_list)
    else:
        r = len(my_list) - 1

    for i in range(0, r, 2):
        one = my_list.pop(i)
        my_list.insert(i+1, one)
    print(my_list)

    """
    Решение от преподавателя
    """
    # for i in range(1, len(my_list), 2):
    #     my_list[i - 1], my_list[i] = my_list[i], my_list[i -1]
    # print(my_list)


def main():
    task_2()


if __name__ == '__main__':
    main()
