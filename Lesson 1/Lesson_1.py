
print(f'{"="*20} Упражнение № 1 {"="*20}')
i = 100
print(i)

var = 'Text, некоторый текст'
print(var)

user_name = input('Ваше имя: ')
user_age = int(input('Ваш возраст? '))

print(f'Привет, пользователь {user_name} возрастом {user_age}!')


########################################
print(f'{"="*20} Упражнение № 2 {"="*20}')
seconds = 0
minutes = 0
hours = 0
user_time_seconds = int(input("Введите время в секундах: "))
seconds = user_time_seconds % 60

if user_time_seconds >= 60:
    if user_time_seconds // 60 >= 60:
        minutes = user_time_seconds // 60

        if minutes >= 60:
            hours = minutes // 60
            minutes = minutes % 60
    else:
        minutes += user_time_seconds // 60
        print(f'minutes: {minutes}')

print(f'{hours}:{minutes:02d}:{seconds:02d}')


########################################
print(f'{"="*20} Упражнение № 3 {"="*20}')
n = int(input('Введите n: '))
sum = n + int(str(n) + str(n)) + int(str(n) + str(n) + str(n))
print(f'n + nn + nnn = {sum}')


########################################
print(f'{"="*20} Упражнение № 4 {"="*20}')

maximum = 0
i = int(input('Введите целое положительное число: '))

if i < 0:
    print('Ошибка, однако! Нужно целое положительное число.')
    exit(-1)

t = i % 10
maximum = t
print(f'max: {maximum}')
d = i // 10
while d > 0:
    # print(f'Целое при делении i на 10: {i} => {d}')
    if d < 10:
        if d > maximum:
            maximum = d
        break
    else:
        ost = d % 10
        if ost > maximum:
            maximum = ost
        print('Переходим к следующей цифре')
    # print(f'max: {max}')
    d = d // 10

print(f'Максимальная цифра в числе {i} - {maximum}')


########################################
print(f'{"="*20} Упражнение № 5 {"="*20}')

revenue = int(input('Введите значение выручки:  '))
costs = int(input('Введите значение издержек: '))
print(f'Вы заработали: {revenue}, издержки составили: {costs}')

delta = revenue - costs
if revenue > costs:
    print(f'Есть прибыль: {delta:+.2f}. Так держать!')
else:
    print(f'Издержки слишком высоки. Убытки: {delta:+.2f}. Давайте сократим программиста.')
    exit(-1)


########################################
print(f'{"="*20} Упражнение № 6 {"="*20}')
efficiency = revenue / costs
print(f'Рентабельность: {efficiency:.2f}')

persons = int(input('Сколько людей у вас работает? '))
eff_per_one = efficiency / persons
print(f'Всего сотрудников: {persons}. Прибыль на одного сотрудника: {eff_per_one:.2f}.')


########################################
print(f'{"="*20} Упражнение № 7 {"="*20}')

result_per_day = int(input('Сколько километров вы пробежали сегодня? '))
goal = int(input('Сколько вы хотели бы уметь бегать? '))
if goal < result_per_day:
    print('Вы уже достигли цели! Поздравляю!')
    exit(-1)

d = 1
while True:
    d += 1
    result_per_day = result_per_day * 1.1
    print(f'{d}-й день: {result_per_day:.2f}')
    if result_per_day > goal:
        # goal_day = round(result_per_day, 0)
        print(f'На {d}-й день спортсмен достиг цели - не менее {goal} километров.')
        break
