from abc import ABC, abstractmethod


class Stationery(ABC):
    def __init__(self, title):
        self.title = title

    @abstractmethod
    def draw(self):
        pass

    @classmethod
    def set_color(cls, color):
        cls.color = color


class Pen(Stationery):
    color = 'blue'

    def draw(self):
        print("Ручка пишет")


class Pencil(Stationery):
    def draw(self):
        print("Карандаш чертит")


class Handle(Stationery):
    def draw(self):
        print("Маркер рисует")


pen = Pen("Ручка")
pencil = Pencil("Карандаш")
handle = Handle("Маркер")

pen.draw()
pencil.draw()
handle.draw()

Stationery.set_color('yellow')
print(Pen.color)
print(Pencil.color)
print(Handle.color)