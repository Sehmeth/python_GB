#4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
#А также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
#конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры,
#общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для каждого
#типа оргтехники.


#5. Продолжить работу над предыдущим заданием. Разработать методы, отвечающие за приём оргтехники
#на склад и передачу в определенное подразделение компании. Для хранения данных о наименовании
#и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру,
#например словарь.


#6.Продолжить работу над предыдущим заданием. Реализуйте механизм валидации вводимых пользователем данных.
#Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип
#данных.Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум
#возможностей, изученных на уроках по ООП.


class Store:

    def __init__(self, name, price, quantity, number_of_lists, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Модель устройства': self.name, 'Цена за шт': self.price, 'Количество': self.quantity}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity}'

    # @classmethod
    # @staticmethod
    def reception(self):
        # print(f'Для выхода - Q, продолжение - Enter')
        # while True:
        try:
            unit = input(f'Введите наименование ')
            unit_p = int(input(f'Цена за шт '))
            unit_q = int(input(f'Введите количество '))
            unique = {'Модель устройства': unit, 'Цена за шт': unit_p, 'Количество': unit_q}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'Список -\n {self.my_store}')
        except:
            return f'Ошибка'

        print(f'Для выхода - Q, продолжение - Enter')
        q = input(f'---> ')
        if q == 'Q' or q == 'q':
            self.my_store_full.append(self.my_store)
            print(f'Склад -\n {self.my_store_full}')
            return f'Выход'
        else:
            return Store.reception(self)


class Printer(Store):
    def to_print(self):
        return f'to print smth {self.numb} times'


class Scanner(Store):
    def to_scan(self):
        return f'to scan smth {self.numb} times'


class Copier(Store):
    def to_copier(self):
        return f'to copier smth  {self.numb} times'


unit_1 = Printer('Canon', 3000, 4, 12)
unit_2 = Scanner('Xerox', 2200, 5, 10)
unit_3 = Copier('НР', 1500, 1, 15)
print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())
print(unit_1.to_print())
print(unit_3.to_copier())