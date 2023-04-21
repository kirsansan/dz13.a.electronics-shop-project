import csv
import math
import os

from constant.constants import CSV_FILE_NAME

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

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
        return f"{self.__class__.__name__}({self.name},{self.price},{self.quantity})"


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

    # @classmethod
    # def discount(cls):
    #     return cls.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(new_name) < 11:
            self.__name = new_name
        else:
            raise ValueError("too many characters in name. it must be less than 10")

    @classmethod
    def instantiate_from_csv(cls):
        """ clear all items from cls
        after clearing fill items from csv file with field name, price and quantity"""
        cls.all = []
        print(" NOW PATH IS ", os.getcwd())
        with open(CSV_FILE_NAME, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cls(row['name'], row['price'], row['quantity'])

    @staticmethod
    def string_to_number(some_string):
        """ Convert string to number with truncation all after dot """
        return math.trunc(float(some_string))
