# Задача 1: Фабрика функций
def create_scaling(op):
    if op == 'squ_func':
        def squ_func(x, y):
            return x ** y

        return squ_func
    elif op == 'int_div':
        def int_div(a, b):
            return a // b

        return int_div


my_func_squ = create_scaling('squ_func')
my_func_div = create_scaling('int_div')
print(f'|Задача 1: Фабрика функций|'
      f'\n{my_func_squ(11, 3)}'
      f'\n{my_func_div(50, 5)}')


# Задача 2: Лямбда-функции
def fl_div_def(x, y):
    return (x // y) / 10


fl_div = lambda x, y: (x // y) / 10
print(f'|Задача 2: Лямбда-функции|'
      f'\n{fl_div(33, 2)}'
      f'\n{fl_div_def(40, 8)}')


# Задача 3: Вызываемые объекты
class Rect:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        return self.a * self.b


area_rect = Rect(14, 12)
print(f'|Задача 3: Вызываемые Объекты|'
      f'\nСтороны прямоугольника: {area_rect.a} и {area_rect.b}'
      f'\nПлощадь: {area_rect.__call__()}')
