import pytest


def test_init_phone(get_test_phone):
    assert get_test_phone.price == 120_000
    assert get_test_phone.quantity == 5
    assert get_test_phone.number_of_sim == 2
    assert str(get_test_phone) == 'iPhone 14'
    assert repr(get_test_phone) == "Phone('iPhone 14', 120000, 5, 2)"


def test_add_phone_and_item(get_test_phone, get_test_item, get_test_keyboard):
    assert get_test_item + get_test_phone == 13
    assert get_test_phone + get_test_phone == 10
    assert get_test_phone + get_test_item == 13
    with pytest.raises(ValueError):
        get_test_phone + get_test_keyboard
    with pytest.raises(ValueError):
        get_test_keyboard + get_test_item


def test_incorrect_number_of_sim(get_test_phone):
    get_test_phone.number_of_sim = 5
    assert get_test_phone.number_of_sim == 5
    with pytest.raises(Exception) as e:
        get_test_phone.number_of_sim = 0
    assert str(e) == str(ValueError("<ExceptionInfo ValueError('invalid number of SIM. it must be more than 0') tblen=2>"))
