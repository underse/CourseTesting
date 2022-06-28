"""
Урок 5. 4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
"""


def main():
    filename = 'Lesson_5_4.txt'
    filename_out = 'Lesson_5_4_result.txt'

    with open(filename, encoding='utf-8') as file:
        file_out = open(filename_out, 'w+', encoding='utf-8')
        for line in file:
            print(line.rstrip())
            num, digit = line.rstrip().split(' — ')
            num = num.strip()
            digit = digit.strip()
            if num == 'One':
                num = 'Один'
            elif num == 'Two':
                num = 'Два'
            elif num == 'Three':
                num = 'Три'
            elif num == 'Four':
                num = 'Четыре'
            s = f'{num} — {digit}'
            print(s)
            file_out.write(s + '\n')


if __name__ == '__main__':
    main()
