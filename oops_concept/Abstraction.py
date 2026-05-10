"""
Abstraction: it will hide the internal implementation, only it will expose necessary details.
Abstraction we can achieve by using ABC module we can achieve.
we cannot create object of the Abstract class.
"""
from abc import ABC, abstractmethod


class House(ABC):

    @abstractmethod
    def base(self):
        pass

    @abstractmethod
    def walls(self):
        pass

    @abstractmethod
    def size(self):
        pass

    def colour_house(self):
        print("red")

class Nandhahouse(House):

    def base(self):
        print("base size:", 3*4)

    def walls(self):
        print("walls size:", 2*1.5)

    def size(self):
        print("House size:", 30*40)

class Veeravenihouse(House):

    def base(self):
        print("base size:", 3*10)

    def walls(self):
        print("walls size:", 3*2)

    def size(self):
        print("size of the house:", 20*40)

# obj = House()
obj = Nandhahouse()
obj.base()
obj.walls()
obj.size()
obj.colour_house()

obj = Veeravenihouse()
obj.base()
obj.size()
obj.walls()
obj.colour_house()
