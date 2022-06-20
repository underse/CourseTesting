"""
Урок 3. Функции.
"""
import sys


def print_header(num):
    print()
    print(f'{"=" * 20} Урок 3. Функции. Упражнение № {num} {"=" * 20}')


def task_1(num):
    print_header(num)

    def task_1_div(a, b):
        return a / b

    a = int(input('Введите число a: '))
    b = int(input('Введите число b: '))

    if b == 0:
        print('Ошибка! b = 0')
        # sys.exit(-1)

    try:
        print(f'{a} / {b} = {task_1_div(1, b):0.4f}')
    except ZeroDivisionError as err:
        print('Ошибка! Деление на 0 (b = 0).')


def task_2(num):
    print_header(num)

    def task_2_show_info(name, surname, borndate, city, email, phone):
        print(f'Пользователь: {name} {surname}\nГод рождения: {borndate}\nГород: {city}\nE-mail: {email}\nТелефон: {phone}')

    name = 'Фома'
    surname = 'Киняев'
    borndate = 1969
    city = 'Москва'
    email = 'master@undergrouund.ru'
    phone = '74951234567'

    task_2_show_info(phone=phone, email=email, name=name, surname=surname, city=city, borndate=borndate)


def task_3(num):
    print_header(num)

    def my_func(a, b, c):
        print(a, b, c)
        l = [a, b, c]
        l.sort()
        print(f'Сумма наибольших чисел {l[1]} + {l[2]} = {l[1] + l[2]}')

    a = int(input('Введите значение "a": '))
    b = int(input('Введите значение "b": '))
    c = int(input('Введите значение "c": '))

    my_func(a, b, c)


def task_4(num):
    print_header(num)

    def my_func(x, y):
        r = 1
        for i in range(abs(y)):
            print(r, x, y)
            r *= x
        if y >= 0:
            return r
        else:
            return 1 / r

    def is_number(s):
        try:
            if s > 0:
                return True
        except ValueError:
            return False
        return False

    def check_y(y):
        try:
            if y >= 0:
                return False
            else:
                return True
        except ValueError:
            return False

    x = float(input('Введите действительное положительное число "x": '))
    y = int(input('Введите целое отрицательное число "y": '))

    if not is_number(x):
        print(f'Ошибка! "x" должен быть действительным положительным числом. Введено: {x}.')
        return False

    if not check_y(y):
        print(f'Ошибка! "y" должен быть целым отрицательным числом. Введено: {y}.')
        return False

    res = my_func(x, y)
    print(f'{x} в степени {y} = {res}')
    print(res)


def task_5(num):
    print_header(num)

    res = 0
    flag = False

    while True:

        s = input('Введите строку чисел разделённых пробелом ("q" для выхода): ').strip()
        if s == 'q':
            print('Выход.')
            break
        elif s.endswith('q'):
            s = s.replace('q', '').strip()
            flag = True

        l = s.split(' ')
        for i, el in enumerate(l):
            l[i] = int(el)
        res += sum(l)
        print(f'Сумма всех чисел: {res}')
        if flag:
            print('Выход.')
            break


def task_6(num):
    print_header(num)

    s = input('Введите одно слово состоящее из маленьких латинских букв [a-z]: ')
    # if ' ' in s:
    #     print('Введено больше одного слова.')
    #     return
    if not check_word_az(s):
        print(f'В слове {s} обнаружены символы кроме [a-z].')
        return

    res = int_func(s)
    print(res)


def task_7(num):
    print_header(num)
    res = ''
    s = input('Введите строку из слов разделённых пробелами. Только символы [a-z ]: ')
    # print(s)

    words = s.split(' ')
    for word in words:
        if len(word) == 0:
            print('Ошибка. Пробелов подряд больше одного.')
            return
        elif not check_word_az(word):
            print(f'В слове "{word}" обнаружены символы кроме [a-z].')
            return
        word = int_func(word)
        if len(res) == 0:
            res = word
        else:
            res = f'{res} {word}'
    print(res)


def int_func(word):
    """
    На входе слово.
    На выходе слово с прописной (заглавной) первой буквой
    :param word:
    :return:
    """
    res = ''
    for i, el in enumerate(word):
        if i == 0:
            el = el.upper()
        res = f'{res}{el}'
    return res


def check_word_az(word):
    for el in word:
        if 97 <= ord(el) <= 122:
            pass
        else:
            return False
    return True


def main():

    task_1(1)
    task_2(2)
    task_3(3)
    task_4(4)
    task_5(5)
    task_6(6)
    task_7(7)


if __name__ == '__main__':
    main()
