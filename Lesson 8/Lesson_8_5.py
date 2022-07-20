"""
     Урок 8. 5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании.
     Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру (например, словарь).
"""


class StorageEquipment:
    def __init__(self, size, number_of_racks, location):
        self.size = size
        self.number_of_racks = number_of_racks
        self.location = location
        self.vault = []
        self.count_items = 0
        print(
            f'Создан класс {self.__class__.__name__}, size={self.size}, number_of_racks={self.number_of_racks}, location={self.location}')

    def __str__(self):
        return (
            f'{self.__class__.__name__}. size={self.size}, number_of_racks={self.number_of_racks}, location={self.location}, vault={self.vault}, count_items={self.count_items}')

    def transfer(self, item, new_class_with_location):
        print(
            f'Товар: {item.properties} перемещён со склада {self.location} на склад: {new_class_with_location.location}.\n')
        self.location = new_class_with_location.location
        new_class_with_location.vault.append(item.properties)
        self.vault.remove(item.properties)

    def add_item(self, item):
        self.vault.append(item.properties)
        self.count_items += 1
        print(f'На склад ({self.location}) принят товар: {item.properties}')
        print(f'Теперь на складе: {self.count_items} товаров.\n')
        print(self.vault)


class Equipment:
    def __init__(self, mass, brand_name, interfaces, count):
        self.properties = {'mass': mass, 'brand_name': brand_name, 'interfaces': interfaces, 'count': count}
        # print(self.properties)


class Printer(Equipment):
    def __init__(self, printer_type, **properties):
        super().__init__(**properties)
        self.properties['printer_type'] = printer_type
        print(f'Создан класс {self.__class__.__name__}: {self.properties}')


class Scanner(Equipment):
    def __init__(self, scanner_type, **properties):
        super().__init__(**properties)
        self.scanner_type = scanner_type
        print(f'Создан класс {self.__class__.__name__}: scanner_type={self.scanner_type}, {self.properties}')


class Copier(Equipment):
    def __init__(self, copies_per_minute, **properties):
        super().__init__(**properties)
        self.copies_per_minute = copies_per_minute
        print(f'Создан класс {self.__class__.__name__}: copies_per_minute={self.copies_per_minute}, {self.properties}')


def main():
    storage_moscow = StorageEquipment(size=1000, number_of_racks=20, location='Moscow')
    storage_tula = StorageEquipment(size=200, number_of_racks=30, location='Tula')

    xerox = Copier(copies_per_minute=10, brand_name='Xerox', mass=4.5, interfaces=['usb 2.0', 'ethernet'], count=3)
    # print(xerox)
    scanner = Scanner(scanner_type='manual', brand_name='Epson', mass=1.4, interfaces=['usb 3.0'], count=5)

    printer = Printer(printer_type='Laser', brand_name='HP', mass=1.9, interfaces=['usb 2.0', 'ethernet'], count=4)
    printer_2 = Printer(printer_type='Ink', brand_name='Canon', mass=2.9, interfaces=['RS-232', 'usd 2.0'], count=1)

    storage_moscow.add_item(scanner)
    storage_moscow.add_item(printer)

    storage_tula.add_item(printer_2)
    storage_tula.add_item(xerox)

    storage_tula.transfer(xerox, storage_moscow)
    print(storage_moscow)


if __name__ == '__main__':
    main()
