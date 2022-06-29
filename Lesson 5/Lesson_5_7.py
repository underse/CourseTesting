"""
Урок 5. 7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли её не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить её в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""
import json


def main():
    filename = 'Lesson_5_7.txt'
    firms_dict = {}
    result = []
    average_profit = {}
    firm_counter = 0
    all_revenue = 0
    with open(filename, encoding='utf-8') as f:
        for line in f.readlines():
            try:
                if line.startswith('#'):
                    continue
                firm_counter += 1
                name, form, gain, costs = line.strip().split(' ')
                print(name, form, gain, costs)
                gain = int(gain)
                costs = int(costs)
                firm_revenue = gain - costs
                print(f'Прибыль: {form} {name}: {firm_revenue}')

                if firm_revenue >= 0:
                    all_revenue += firm_revenue
                firms_dict[name] = firm_revenue
                print()
            except ValueError as e:
                print('\nОшибка чтения из файла! Проверьте правильность исходного файла.\nДолжно быть четыре поля в каждой строке.\nНапример: firm_1 ООО 10000 5000')
    avg_profit = firm_revenue / firm_counter
    print(f'Средняя прибыль по {firm_counter} компаниям: {avg_profit}')

    print(firms_dict)
    result.append(firms_dict)
    average_profit['average_profit'] = avg_profit
    result.append(average_profit)
    print(result)

    with open('Lesson_5_7.json', 'w+') as f:
        json.dump(result, f)


if __name__ == '__main__':
    main()
