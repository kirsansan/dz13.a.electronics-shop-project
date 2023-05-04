from constant.constants import LANG_LIST


class ChangeLangMixin:

    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        self.__lang = "EN"

    def change_lang(self):
        """Change the language from LANG_LIST
        to anything non-equal to the current language
        """
        for challenger in LANG_LIST:
            if self.__lang != challenger:
                self.__lang = challenger
                break
        return self

    @property
    def language(self):
        return self.__lang
