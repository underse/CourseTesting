"""
Урок 2. 5.
"""


def print_header(num):
    print()
    print(f'{"=" * 20} Упражнение № {num} {"=" * 20}')


def task_5():
    print_header(5)
    my_list = [9, 8, 7, 7, 5, 3]
    done = False
    new = int(input('Введите новый элемент рейтинга: '))
    print('Текущий рейтинг: ', my_list)

    pos = 0
    ins = False

    for el in my_list:
        if new > el:
            my_list.insert(pos, new)
            done = True
            break
        elif new == el:
            ins = True
        elif ins and new < el:
            my_list.insert(pos, new)
            break
        pos += 1

    if not done:
        my_list.insert(pos, new)

    print('Новый рейтинг: ', my_list)


def main():
    task_5()


if __name__ == '__main__':
    main()
