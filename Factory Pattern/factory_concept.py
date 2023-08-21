# pylint: disable=too-few-public-methods
# pylint: disable=arguments-differ
"The Factory Concept"
from abc import ABCMeta, abstractmethod


class IProduct(metaclass=ABCMeta):
    "A Hypothetical Class Interface (Product)"

    @staticmethod
    @abstractmethod
    def create_object():
        "An abstract interface method"


class ConcreteProductA(IProduct):
    "A Concrete Class that implements the IProduct interface"

    def __init__(self):
        self.name = "Concrete Product A"

    def create_object(self):
        return self


class ConcreteProductB(IProduct):
    "A Concrete Class that implements the IProduct interface"

    def __init__(self):
        self.name = "Concrete Product B"

    def create_object(self):
        return self


class ConcreteProductC(IProduct):
    "A Concrete Class that implements the IProduct interface"

    def __init__(self):
        self.name = "Concrete Product C"

    def create_object(self):
        return self


class Creator:
    "The Factory Class"

    @staticmethod
    def create_object(some_property):
        "A static method to get a concrete product"

        if some_property == "a":
            return ConcreteProductA()
        if some_property == "b":
            return ConcreteProductB()
        if some_property == "c":
            return ConcreteProductC()


PRODUCT = Creator().create_object("a")
print(PRODUCT.name)
