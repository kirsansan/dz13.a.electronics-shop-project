from src.item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim  # type: ignore

    def __repr__(self):
        tmp_str = super().__repr__()
        tmp_str = tmp_str.replace(")", f", {self.number_of_sim})")
        return tmp_str

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        raise ValueError('You must sum only object of classes Item and Phone')

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, new_number):
        if new_number > 0:
            self.__number_of_sim = new_number
        else:
            raise ValueError("invalid number of SIM. it must be more than 0")


if __name__ == '__main__':
    # смартфон iPhone 14, цена 120_000, количество товара 5, симкарт 2
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    item1 = Item("Смартфон", 10000, 20)

    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10
    assert phone1 + item1 == 25
    item1 + 5  # ValueError
    phone1 + 6  # ValueError
