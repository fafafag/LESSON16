from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, color, name, age):
        self.color = color
        self.name = name
        self.age = age

    @abstractmethod
    def say(self):
        pass


class Cat(Animal):
    def say(self):
        return 'Meow!'


class Dog(Animal):
    def say(self):
        return 'Woof!'


cat = Cat('black', 'Kitty', 2)
dog = Dog('brown', 'Buddy', 4)

print(f'{cat.name} ({cat.color}, {cat.age} year(s) old) says {cat.say()}')
print(f'{dog.name} ({dog.color}, {dog.age} year(s) old) says {dog.say()}')