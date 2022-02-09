#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):

    def test_plus_name(self):
        """
        return: None
        test if the result is equal to specified value
        """
        plus = [Item('+5 Dexterity Vest', 10, 20)]
        gilded_rose = GildedRose(plus)
        gilded_rose.update_quality()
        self.assertEqual('+5 Dexterity Vest', plus[0].name)

    def test_brie_sell_in(self):
        """
        return: None
        test if the result is equal to specified value
        """
        brie = [Item('Aged Brie', 2, 0)]
        gilded_rose = GildedRose(brie)
        gilded_rose.update_quality()
        self.assertEqual(1, brie[0].sell_in)

    def test_elixir_sell_in(self):
        """
        return: None
        test if the result is equal to specified value
        """
        elixir = [Item('Elixir of the Mongoose', 5, 7)]
        gilded_rose = GildedRose(elixir)
        gilded_rose.update_quality()
        self.assertEqual(4, elixir[0].sell_in)

    def test_sulfuras_quality(self):
        """
        return: None
        test if the result is equal to specified value
        """
        sulfuras = [Item('Sulfuras, Hand of Ragnaros', 0, 80)]
        gilded_rose = GildedRose(sulfuras)
        gilded_rose.update_quality()
        self.assertEqual(80, sulfuras[0].quality)

    def test_backstage_quality(self):
        """
        return: None
        test if the result is equal to specified value
        """
        backstage = [Item('Backstage passes to a TAFKAL80ETC concert', 0, 20)]
        gilded_rose = GildedRose(backstage)
        gilded_rose.update_quality()
        self.assertEqual(0, backstage[0].quality)

    def test_conjured_quality(self):
        """
        return: None
        test if the result is equal to specified value
        """
        conjured = [Item('Conjured Mana Cake', 3, 6)]
        gilded_rose = GildedRose(conjured)
        gilded_rose.update_quality()
        self.assertEqual(4, conjured[0].quality)


if __name__ == '__main__':
    unittest.main()
