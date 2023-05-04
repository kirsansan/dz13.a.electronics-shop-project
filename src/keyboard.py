from src.item import Item
from src.change_lang import ChangeLangMixin


class KeyBoard(ChangeLangMixin, Item):
    def __set_allow_summ(self):
        """ fill type(subclass) to Item.classes_allowed_to_summ
            if subclass want be able to sum with Item elements this method need to be rewrite as
            'if type(self) not in Item.classes_allowed_to_summ:
                Item.classes_allowed_to_summ.append(type(self))'"""
        pass
