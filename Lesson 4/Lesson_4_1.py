import sys


def calc_salary(hours, rate, bonus):
    return (hours*rate) + bonus


def main():

    try:
        hours = float(sys.argv[1])
        rate = float(sys.argv[2])
        bonus = float(sys.argv[3])
    except IndexError as e:
        print('Запуск с параметрами:')
        print(f'{sys.argv[0]} hours rate_per_hour bonus')

    print(f'Выработка в часах: {hours:.2f}')
    print(f'ставка в час: {rate:.2f}')
    print(f'Премия: {bonus:.2f}')

    print(f'\nИтого, заработная плата: {calc_salary(hours, rate, bonus):.2f} у.е.')

if __name__ == '__main__':
    main()
