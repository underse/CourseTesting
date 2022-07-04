"""
    Урок 6. 4. Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.
"""


class Car:
    def __init__(self, speed: int, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.__class__.__name__} {self.name} поехала.')

    def stop(self):
        print(f'{self.__class__.__name__} {self.name} остановилась.')

    def turn(self, direction):
        print(f'{self.__class__.__name__} {self.name} поворачивает: {direction}.')

    def show_speed(self):
        print("""  ______
 /|_||_\`.__
(   _    _ _\\
=`-(_)--(_)-'""")
        print(f'{self.__class__.__name__} скорость: {self.speed}')


class TownCar(Car):
    def __init__(self, speed: int, color, name):
        super().__init__(speed, color, name, False)
        self.max_speed = 60
        print(f'Создан класс {self.__class__.__name__}, скорость: {speed}, {color} {name}, is_police={self.is_police}')

    def show_speed(self):
        print("""     ___________________________
  _ //~~~~~~~~~~~~~|------|-----\    |
_|_/-------------/_|______|_______\__|________,_
  \ _@_______________|____-_|-______|_____________)
   <____//   \|______|______|_______|_//   \)_____>
         \___/                         \___/""")
        if self.speed > self.max_speed:
            print(f'Внимание! Превышение скорости! {self.speed} (max: {self.max_speed})')


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)
        print(f'Создан класс {self.__class__.__name__}, скорость: {speed}, {color} {name}, is_police={self.is_police}')


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)
        self.max_speed = 40
        print(f'Создан класс {self.__class__.__name__}, скорость: {speed}, {color} {name}, is_police={self.is_police}')

    def show_speed(self):
        print("""   ---------------------------.
 `/""""/""""/|""|'|""||""|   ' \.
 /    /    / |__| |__||__|      |
/----------=====================|
| \  /V\  /    _.               |
|()\ \W/ /()   _            _   |
|   \   /     / \          / \  |-( )
=C========C==_| ) |--------| ) _/==] _-{_}_)
 \_\_/__..  \_\_/_ \_\_/ \_\_/__.__.""")
        if self.speed > self.max_speed:
            print(f'Внимание! Превышение скорости! {self.speed} (max: {self.max_speed})')


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)
        print(f'Создан класс {self.__class__.__name__}, скорость: {speed}, {color} {name}, is_police={self.is_police}')


def main():
    sport_1 = SportCar(150, 'красный', 'Порш турбо')
    sport_1.show_speed()
    sport_1.go()
    sport_1.speed = 240
    sport_1.show_speed()
    sport_1.stop()

    police_1 = PoliceCar(250, 'синий', 'Полиция_330')

    police_2 = PoliceCar(200, 'белый', 'Полиция_111')
    police_2.show_speed()
    police_2.go()
    police_2.turn('налево')

    police_1.turn('направо')
    police_1.go()
    police_1.stop()

    police_2.stop()
    police_2.turn('направо')

    town_1 = TownCar(50, 'чёрный', 'Линкольн континенталь')
    work_1 = WorkCar(30, 'жёлтый', 'Автобус ПАЗ')

    town_1.go()
    town_1.show_speed()
    town_1.turn('налево')
    town_1.speed = 70
    town_1.show_speed()

    work_1.show_speed()
    work_1.go()
    work_1.speed = 55
    work_1.show_speed()
    work_1.stop()


if __name__ == '__main__':
    main()
