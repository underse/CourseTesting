import sys


def print_header(num):
    print()
    print(f'{"=" * 20} Упражнение № {num} {"=" * 20}')


def task_1():
    print_header(1)
    my_list1 = [1, 'abc', {'key1': 123, 'key99': 99999}, True, False, (2, 6, 10)]
    for el in my_list1:
        print(type(el))


def task_2():
    print_header(2)
    my_list = input('Введите элементы списка разделённые одним пробелом: ').split(' ')
    print(my_list)

    i = 0

    # обработка чётности/нечётности
    if len(my_list) % 2 == 0:
        r = len(my_list)
    else:
        r = len(my_list) - 1

    for i in range(0, r, 2):
        one = my_list.pop(i)
        my_list.insert(i+1, one)
    print(my_list)


def task_3():
    print_header(3)
    month = int(input('Введите значение месяца в виде целого числа от 1 до 12: '))

    year = {'зима': [1, 2, 12], 'весна': [3, 4, 5], 'лето': [6, 7, 8], 'осень': [9, 10, 11]}
    for key, value in year.items():
        if month in value:
            print(f'Месяц № {month} относится ко времени года: {key}.')


def task_4():
    print_header(4)
    my_str = input('Введите строку разделённую пробелами: ')
    i = 1
    for word in my_str.split(' '):
        print(f'{i:5d}\t{word:.10}')
        i += 1


def task_5():
    print_header(5)


def main():
    ########################################
    task_1()

    task_2()

    task_3()

    task_4()

    # task_5()

if __name__ == '__main__':
    main()
