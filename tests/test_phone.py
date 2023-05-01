import pytest

from src.phone import Phone


def test_init_phone(get_test_phone, get_test_item):
    assert get_test_phone.price == 120_000
    assert get_test_phone.quantity == 5
    assert get_test_phone.number_of_sim == 2
    assert str(get_test_phone) == 'iPhone 14'
    assert repr(get_test_phone) == "Phone('iPhone 14', 120000, 5, 2)"

