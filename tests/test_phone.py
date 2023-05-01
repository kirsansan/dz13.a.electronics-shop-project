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
    assert get_test_phone + get_test_keyboard == None
    assert get_test_keyboard + get_test_item == None


def test_incorrect_number_of_sim(get_test_phone):
    get_test_phone.number_of_sim = 5
    assert get_test_phone.number_of_sim == 5

    with pytest.raises(Exception):
        get_test_phone.number_of_sim = 0

    try:
        get_test_phone.number_of_sim = 0
    except ValueError as e:
        assert str(e) == str(ValueError('invalid number of SIM. it must be more than 0'))
