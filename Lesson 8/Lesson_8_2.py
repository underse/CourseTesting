"""
     Урок 8. 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""
import random


class MyError(Exception):
    def __init__(self, text):
        self.txt = text


def main():
    while True:
        r = random.randint(1, 99)
        print(f'Произвольное число: {r}. На сколько будем его делить?')
        a = input('\nВведите число (для прекращения наберите "stop"): ')
        if a == 'stop':
            print('STOP. Прекращение работы.')
            break

        try:
            a = int(a)
            if a == 0:
                raise MyError('На "0" делить нельзя!')
            res = r / a
            print(res)
        except MyError as mr:
            print(mr)


if __name__ == '__main__':
    main()
