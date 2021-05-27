class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print ('Запуск отрисовки')

class Pen(Stationery):

    def __init__(self, title):
        self.title = title

    def draw(self):
        print (f'Штриховка при помощи инструмента {self.title}')

class Pencil(Stationery):

    def __init__(self, title):
        self.title = title

    def draw(self):
        print (f'Чертеж контура при помощи инструмента {self.title}')

class Handle(Stationery):

    def __init__(self, title):
        self.title = title

    def draw(self):
        print (f'Обводка контура при помощи инструмента {self.title}')

black_pen = Pen('черная ручка')
thick_pencil = Pencil('тонкий карандаш')
red_handle = Handle('красный маркер')

black_pen.draw()
thick_pencil.draw()
red_handle.draw()
