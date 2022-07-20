"""
     Урок 8. 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
     В рамках класса реализовать два метода.
     Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
     Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
     Проверить работу полученной структуры на реальных данных.
"""

from datetime import datetime


class Date:
    def __init__(self):
        pass

    @classmethod
    def convert_to_int(cls, date):
        d = datetime.strptime(str(date).replace('-', ''), '%Y%m%d')
        # print(d)
        a = int(d.strftime('%Y%m%d'))
        print(f'Date: {date} => {a}')
        return a

    @staticmethod
    def validate(date):
        is_valid_date = True
        try:
            (year, month, day) = date.split('-')
            datetime(int(year), int(month), int(day))
            print(f'Дата верная: {date}. ')
        except ValueError:
            print(f'Ошибка! Неверная дата: {date}.')
            is_valid_date = False
        return is_valid_date


def main():
    d1 = Date()
    # d1.validate()
    d1.convert_to_int('2022-07-10')

    d2 = Date()
    d2.validate('2022-13-10')

    d3 = Date()
    d3.validate('2022-02-30')

    d4 = Date
    d4.validate('2022-02-28')


if __name__ == '__main__':
    main()
