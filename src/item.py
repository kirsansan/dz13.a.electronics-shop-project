import csv
import math
from constant.constants import CSV_FILE_NAME
from src.csv_error import InstantiateCSVError


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all: list = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.name}"

    def __add__(self, other):
        condition1: bool = issubclass(type(other), type(self))
        condition2: bool = issubclass(type(self), type(other))
        if condition1 or condition2:
            return self.quantity + other.quantity
        raise ValueError('You must sum only object of classes Item and its subclasses')

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return round(self.price * self.quantity)

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        print("price", self.price)
        print("discount", self.__class__.pay_rate)
        self.price = round(self.price * self.__class__.pay_rate)

    @classmethod
    def set_discount(cls, new_discount):
        """set the discount for all items"""
        cls.pay_rate = new_discount

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(new_name) < 11:
            self.__name = new_name
        else:
            raise ValueError("too many characters in name. it must be less than 11")

    @classmethod
    def instantiate_from_csv(cls, path=CSV_FILE_NAME):
        """ clear all items from cls
        after clearing we are going fill items from csv file with fields 'name', 'price' and 'quantity'"""
        cls.all = []
        try:
            with open(path, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                try:
                    for row in reader:
                        cls(row['name'], row['price'], row['quantity'])
                except KeyError:
                    raise InstantiateCSVError("item.csv file is corrupted")
        except FileNotFoundError:
            raise FileNotFoundError("file items.csv does not exist or bad directory")

    @staticmethod
    def string_to_number(some_string):
        """ Convert string to number with truncation all digits after dot """
        return math.trunc(float(some_string))
