import pytest
from src.item import Item
from src.phone import Phone
from src.keyboard import KeyBoard

item1_for_test = Item(name='NAME1', price=5, quantity=8)
item2_for_test = Item(name='NAME_not1', price=500, quantity=10)
item1_for_test.pay_rate = 0.1

CSV_NON_CORRECT_FILE_NAME = "../src/items-no-exist.csv"
CSV_CORRUPTED_FILE = "../src/items_bad.csv"


@pytest.fixture
def get_test_item():
    return item1_for_test


@pytest.fixture
def get_test_all():
    return item2_for_test.all


phone1_for_test = Phone("iPhone 14", 120_000, 5, 2)
kb_for_test = KeyBoard('Dark Project KD87A', 9600, 5)


@pytest.fixture
def get_test_phone():
    return phone1_for_test


@pytest.fixture
def get_test_keyboard():
    return kb_for_test


@pytest.fixture
def get_non_exist_file_name():
    return CSV_NON_CORRECT_FILE_NAME


@pytest.fixture
def get_corrupted_file():
    return CSV_CORRUPTED_FILE
