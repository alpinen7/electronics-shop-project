"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

item_1 = Item("Чехол", 200, 10)

def test_calculate_total_price():
    assert item_1.calculate_total_price() == 2000

def test_apply_discount():
    assert item_1.apply_discount() == None




