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
    my_list = [9, 8, 7, 7, 5, 3]
    done = False
    new = int(input('Введите новый элемент рейтинга: '))
    print('Текущий рейтинг: ', my_list)

    pos = 0
    for el in my_list:
        if new >= el:
            my_list.insert(pos, new)
            done = True
            break
        pos += 1

    if not done:
        my_list.insert(pos, new)

    print('Новый рейтинг: ', my_list)


def task_6():
    print_header(6)
    goods = []
    # unit1 = (1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'ед': 'шт.'})
    # unit2 = (2, {'название': 'принтер', 'цена': 5000, 'количество': 3, 'ед': 'шт.'})
    # goods.append(unit1)
    # goods.append(unit2)
    # print(goods)

    num = 0
    print_help()
    while True:
        num += 1

        print()
        print(f'Товар № {num}')

        name = get_input('Название: ')
        if name == '':
            break

        price = get_input('Цена: ')
        if price == '':
            break
        price = int(price)

        count = get_input('Количество: ')
        if count == '':
            break
        count = int(count)

        measure = get_input('Единица измерения: ')
        if measure == '':
            break

        if name != '' and measure != '' and price != -1 and count != -1:
            unit = {'название': name, 'цена': price, 'количество': count, 'ед': measure}
            print(f'Добавлен товар № {num}: {unit}')
            goods.append((num, unit))

    print('Ввод информации о товарах закончен.')
    print(goods)

    start_analytics(goods)


def get_input(message):
    return input(message)


def start_analytics(goods):
    res = {}
    print()
    print('Сбор аналитики о товарах.')
    for good in goods:
        for key, value in good[1].items():
            # print(key, value)
            if key not in res:
                res[key] = [value]
            else:
                res[key].append(value)
    res['ед'] = list(set(res['ед']))
    print('Вот что получилось собрать:')
    print(res)


def print_help():
    print('Введите пустое значение для прекращения ввода. Будут сохранены только полностью введённые данные о товаре.')


def main():
    task_1()
    task_2()
    task_3()
    task_4()
    task_5()
    task_6()


if __name__ == '__main__':
    main()
