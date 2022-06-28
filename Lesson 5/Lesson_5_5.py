"""
Урок 5. 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
"""



def main():
    filename = 'Lesson_5_5.txt'

    s = input('Введите числа разделённые пробелами: ')
    digits_list = s.split(' ')

    with open(filename, 'w+', encoding='utf-8') as f:
        f.write(s)

    print(f'Введённые числа: {digits_list} записаны в файл: {filename}')

    with open(filename, 'r', encoding='utf-8') as f:
        digits_list2 = [float(x) for x in f.read().split(' ')]
        print(f'Прочитаны из файла: {filename} числа: {digits_list2}')
        digits_sum = sum(digits_list2)
        print(f'Сумма чисел из файла {filename}: {digits_sum}')


if __name__ == '__main__':
    main()
