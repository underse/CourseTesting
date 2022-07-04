"""
    Урок 6. 1. Создать класс TrafficLight (светофор).
определить у него один атрибут color (цвет) и метод running (запуск);
атрибут реализовать как приватный;
в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов.
При его нарушении выводить соответствующее сообщение и завершать скрипт.
"""

from time import sleep


class TrafficLight:
    def __init__(self, color='red'):
        self.__color = color
        self.__switch = 0

    def running(self):
        while True:
            if self.__switch == 10:
                print('Светофору пора на техобслуживание.')
                break
            if self.__color == 'red':
                print('Красный на 7 секунд.')
                sleep(7)
                self.__switch += 1
                self.__color = 'yellow'
                self.running()
            elif self.__color == 'yellow':
                print('Жёлтый на 2 секунды.')
                sleep(2)
                self.__switch += 1
                self.__color = 'green'
                self.running()
            elif self.__color == 'green':
                print('Зелёный на 5 секунд.')
                sleep(5)
                self.__switch += 1
                self.__color = 'red'
                self.running()


def main():
    traffic_light = TrafficLight()
    traffic_light.running()


if __name__ == '__main__':
    main()
