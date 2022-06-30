"""
Урок 2. 6.
"""


def print_header(num):
    print()
    print(f'{"=" * 20} Упражнение № {num} {"=" * 20}')


def print_help():
    print('Введите пустое значение для прекращения ввода. Будут сохранены только полностью введённые данные о товаре.')


def get_input(message):
    return input(message)


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


def main():
    task_6()


if __name__ == '__main__':
    main()
