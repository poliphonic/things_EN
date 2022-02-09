#!/usr/bin/env python
# -*- coding: utf-8 -*-


class GildedRose(object):

    def __init__(self, items):
        """
        items: a list of items
        """
        self.items = items

    def update_quality(self):
        """
        return: None
        change item.sell_in and item.quality
        """
        aged = 'Aged Brie'
        backstage = 'Backstage passes to a TAFKAL80ETC concert'
        conjured = 'Conjured Mana Cake'
        sulfuras = 'Sulfuras, Hand of Ragnaros'
        for item in self.items:
            item.sell_in -= 1

            if item.name == aged or item.name == backstage:
                item.quality += 1
                if item.name == backstage and 0 <= item.sell_in <= 5:
                    item.quality += 2
                elif item.name == backstage and 5 < item.sell_in <= 10:
                    item.quality += 1
            elif item.name == conjured:
                item.quality -= 2 if item.sell_in >= 0 else 4
            elif item.name == sulfuras:
                item.sell_in += 1
                item.quality = 80
            else:
                item.quality -= 1 if item.sell_in >= 0 else 2

            if item.quality < 0 or item.name == backstage and item.sell_in < 0:
                item.quality = 0
            elif item.quality > 50 and not item.name == sulfuras:
                item.quality = 50


class Item:

    def __init__(self, name, sell_in, quality):
        """
        name: a string
        sell_in: an integer
        quality: an integer
        """
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return '{}, {}, {}'.format(self.name, self.sell_in, self.quality)
