import pytest
from src.item import Item
from src.csv_error import InstantiateCSVError


def test_init_item(get_test_item, get_test_all):
    assert get_test_item.price == 5
    assert get_test_item.quantity == 8
    assert get_test_all[1].pay_rate == 1.0


def test_print_all(get_test_all):
    assert repr(get_test_all) == """[Item('NAME1', 5, 8), Item('NAME_not1', 500, 10), Phone('iPhone 14', 120000, 5, 2), KeyBoard('Dark Project KD87A', 9600, 5)]"""


def test_print(get_test_item):
    assert repr(get_test_item) == "Item('NAME1', 5, 8)"
    assert str(get_test_item) == 'NAME1'


def test_calculate_total_price(get_test_item):
    assert get_test_item.calculate_total_price() == 40


def test_set_discount(get_test_item):
    new_item = get_test_item
    assert new_item.price == 5
    new_item.pay_rate == 0.1  # it's not Class discount, only local class instance
    assert new_item.pay_rate == 0.1
    new_item.apply_discount()
    assert new_item.price == 5  # we don't have changes!!

    new_item.set_discount(0.3)  # now we have been changing
    new_item.apply_discount()
    assert new_item.price == 2


def test_naming(get_test_item):
    new_item = get_test_item
    assert new_item.name == "NAME1"
    new_item.name = "NAME_100"
    assert new_item.name == "NAME_100"
    with pytest.raises(Exception):
        new_item.name = "NAME_WITH_LONG_STRING"


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
    assert repr(
        Item.all) == """[Item('Смартфон', 100, 1), Item('Ноутбук', 1000, 3), Item('Кабель', 10, 5), Item('Мышка', 50, 5), Item('Клавиатура', 75, 5)]"""

def test_instantiate_from_bad_csv_file(get_non_exist_file_name, get_corrupted_file):
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv(path=get_non_exist_file_name)
    try:
        Item.instantiate_from_csv(path=get_non_exist_file_name)
    except FileNotFoundError as e:
        assert str(e) == 'file items.csv does not exist or bad directory'
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv(path=get_corrupted_file)
    try:
        Item.instantiate_from_csv(path=get_corrupted_file)
    except InstantiateCSVError as e:
        assert str(e) == 'item.csv file is corrupted'
    assert len(Item.all) == 0
    assert Item.all == []

def test_add_subclass(get_test_item):
    assert get_test_item + get_test_item == 16
    with pytest.raises(ValueError):
        get_test_item + 5
    try:
        get_test_item + 8
    except ValueError as e:
        assert str(e) == str(ValueError('You must sum only object of classes Item and its subclasses'))
