import unittest
from lab02_sklep import Shop
import io
import sys


class TestShop(unittest.TestCase):
    def setUp(self):
        self.shop = Shop("baza_danych.txt")

    def test_load_data(self):
        self.shop.load_data()
        self.assertEqual(self.shop.products, {'Komputer': 10, 'Laptop': 20})
        self.assertEqual(self.shop.customers, {'Jan_Kowalski': {}, 'Anna_Nowak': {}})

    def test_sell_positive_quantity(self):
        self.shop.load_data()
        self.shop.sell("sell Jan_Kowalski:Komputer(2): Anna_Nowak:Komputer(1)")
        self.assertEqual(self.shop.products, {'Komputer': 7, 'Laptop': 20})
        self.assertEqual(self.shop.customers, {'Jan_Kowalski': {'Komputer': 2}, 'Anna_Nowak': {'Komputer': 1}})

    def test_sell_negative_quantity(self):
        self.shop.load_data()
        self.shop.sell("sell Jan_Kowalski:Komputer(-2) Anna_Nowak:Laptop(-1)")
        self.assertEqual(self.shop.products, {'Komputer': 10, 'Laptop': 20})
        self.assertEqual(self.shop.customers, {'Jan_Kowalski': {}, 'Anna_Nowak': {}})

    def test_sell_insufficient_quantity(self):
        self.shop.load_data()
        self.shop.sell("sell Jan_Kowalski:Komputer(20) Anna_Nowak:Laptop(25)")
        self.assertEqual(self.shop.products, {'Komputer': 10, 'Laptop': 20})
        self.assertEqual(self.shop.customers, {'Jan_Kowalski': {}, 'Anna_Nowak': {}})


if __name__ == '__main__':
    unittest.main()
