"""Модуль тестирования сериализации JSON."""

from json_serializer import loads, dumps, dump, load


f = 16


def HELLO():
    """Метод для тестирования сериализации функции."""
    if(f == 16):
        print('HELLO')


a = []
a.append(dict(int_list=[1, 2, 3], str_list=['a', 'b', 'c'],
         dick=dict([('1', 2)]), text='string', number=3.44,
         boolean=True, none=None))
a.append([[1, 2, 3], ['a', 'b', 'c'], dict([('1', 1), ('2', 2)]),
         'string', 3.44, True, None])
a.append([[1, 2, 3], 3.44, ['a', 'b', 'c'], True,
         dict([('1', 1), ('2', 2)]), 'string', None])
a.append(dict(int_list=[1, 2, 3], number=3.44, str_list=['a', 'b', 'c'],
         boolean=True, dick=dict([('1', 2)]), text='string', none=None))
a.append([[[1, 2, 3], ['a', 's', 'd'], [1, 2, 3]],
         [[4, 5, 6], ['f', 'g', 'h'], [4, 5, 6]]])
a.append(dict(a1=dict(a11=11, a12=12), a2=dict(a21=21, a22=22)))
a.append([[[1], ['a'], [2]], [[4], ['f'], [5]], 6])
a.append(dict(a11=[dict(a111=[111]), 123], a12=12))
a.append([[[1, 2, 3], 2]])
a.append((100, (1, 2, 3), 3))
A = a

b = dumps(A)
c = loads(b)
dump(A, './json_files/data1.json', 1)
print(load('./json_files/data1.json'))
print(c, 'my_loads')

print()

asa = dumps(HELLO, 1)
dump(HELLO, './json_files/data2.json', 1)
load('./json_files/data2.json', 1)()
loads(asa, 1)()
print()


class TestClass:
    """тестовый класс."""

    def __init__(self):
        """Метод инициализации класса."""
        pass
    test_int = 12345
    test_float = 3.14
    test_tuple = (1, 2, 3)
    test_string = 'Test String'
    test_none = None
    test_bool = False

    def HELLO1(self):
        """Тестовый Метод класса."""
        if(f == 16):
            print('HELLO1')

    def sas(self, i):
        """Тестовый Метод класса."""
        self.test_int += i


tempclass = dumps(TestClass)
a = loads(tempclass, 1)

dump(TestClass, './json_files/data3.json', 1)
asdf = load('./json_files/data3.json', 1)
asdf.HELLO1(asdf)

b = TestClass()
b = a()
a.HELLO1(a)
b.HELLO1()
print(b.test_bool)
