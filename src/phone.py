from src.item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim  # type: ignore

    def __repr__(self):
        tmp_str = super().__repr__()
        tmp_str = tmp_str.replace(")", f", {self.number_of_sim})")
        return tmp_str

    # def __add__(self, other):
    #     if isinstance(other, self.__class__) or type(other) == type(self):
    #         return self.quantity + other.quantity


    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, new_number):
        if new_number > 0:
            self.__number_of_sim = new_number
        else:
            raise ValueError("invalid number of SIM. it must be more then 0")