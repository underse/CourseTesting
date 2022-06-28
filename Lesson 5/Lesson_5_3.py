"""
Урок 5. 3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""


def main():
    filename = 'Lesson_5_3_personal.txt'
    avg = 0
    fund = 0
    personal_count = 0
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            surname, salary = line.strip().split(' ')
            salary = float(salary)
            fund += salary
            personal_count += 1
            if salary < 20000:
                print(f'{surname} <20000.00 ({salary:.2f})')

    print(f'Средний доход: {fund/personal_count:.2f}')


if __name__ == '__main__':
    main()
