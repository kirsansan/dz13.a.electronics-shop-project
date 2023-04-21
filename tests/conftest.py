import pytest
from src.item import Item

item1_for_test = Item(name='NAME1', price=5, quantity=8)
item2_for_test = Item(name='NAME_not1', price=500, quantity=10)
item1_for_test.pay_rate = 0.1


@pytest.fixture
def get_test_item():
    return item1_for_test


@pytest.fixture
def get_test_all():
    return item2_for_test.all
