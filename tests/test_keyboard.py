import pytest

def test_keyboard_init(get_test_keyboard):
    assert str(get_test_keyboard) == "Dark Project KD87A"
    assert str(get_test_keyboard.language) == "EN"


def test_keyboard_change_lang(get_test_keyboard):
    assert str(get_test_keyboard.language) == "EN"
    get_test_keyboard.change_lang()
    assert str(get_test_keyboard.language) == "RU"
    get_test_keyboard.change_lang().change_lang()
    assert str(get_test_keyboard.language) == "RU"


def test_keyboard_incorrect_set_lang(get_test_keyboard):
    with pytest.raises(AttributeError) as err:
        get_test_keyboard.language = "US"
    assert str(err) == "<ExceptionInfo AttributeError(\"can't set attribute 'language'\") tblen=1>"
    # it's strange but is task we have to handle other message
    # AttributeError: property 'language' of 'KeyBoard' object has no setter
