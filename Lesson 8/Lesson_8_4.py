"""
     Урок 8. 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
     А также класс «Оргтехника», который будет базовым для классов-наследников.
     Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
     В базовом классе определите параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.
"""


# class MyError(Exception):
#     def __init__(self, text):
#         self.txt = text


class StorageEquipment:
    def __init__(self, size, number_of_racks, location, count):
        self.size = size
        self.number_of_racks = number_of_racks
        self.location = location
        self.count = count


class Equipment:
    def __init__(self, mass, brand_name, interface, count):
        self.mass = mass
        self.brand_name = brand_name
        self.interface = interface
        self.count = count


class Printer(Equipment):
    def __init__(self, printer_type, mass, brand_name, interface, count):
        # super().__init__(mass, brand_name, interface, count)
        self.printer_type = printer_type


class Scanner(Equipment):
    def __init__(self, scanner_type, mass, brand_name, interface, count):
        # super().__init__(mass, brand_name, interface, count)
        self.scanner_type = scanner_type


class Copier(Equipment):
    def __init__(self, copies_per_minute):
        self.copies_per_minute = copies_per_minute


def main():
    pass


if __name__ == '__main__':
    main()
