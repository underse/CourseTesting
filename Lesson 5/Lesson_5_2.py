"""
Урок 5. 2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.
"""


def main():
    filename = 'Lesson_5_2.txt'
    print(f'Файл: {filename}')
    with open(filename, 'r') as f:
        lines = f.readlines()
        line_num = 0
        for line in lines:
            line_num += 1
            words = line.split(' ')
            words_count = len(words)
            print(f'Строка: {line_num}. Слов: {words_count}')

    print(f'Строк: {len(lines)}')


if __name__ == '__main__':
    main()
