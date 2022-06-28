"""
Урок 5. 6. Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать учебный предмет и наличие лекционных, практических и лабораторных занятий по предмету.
Сюда должно входить и количество занятий. Необязательно, чтобы для каждого предмета были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.
Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""


def main():
    filename = 'Lesson_5_6.txt'
    d = {}
    with open(filename, encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            print(line.strip())
            name, subjects = line.rstrip().split(':')
            # print(name, '***', subjects)
            subjects_list = subjects.strip().split(' ')
            subject_count = 0
            for subject in subjects_list:
                try:
                    s = int(str(subject.split('(')[0]))
                    subject_count += s
                except ValueError as e:
                    pass
                # print(f's: {subject_count}')
                d[name.strip()] = subject_count
    print(f'd: {d}')


if __name__ == '__main__':
    main()
