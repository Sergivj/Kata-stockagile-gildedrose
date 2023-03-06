# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    @staticmethod
    def aged_brie(item):
        if item.quality < 50:
            item.quality = item.quality + 1
        item.sell_in = item.sell_in - 1

    @staticmethod
    def sulfuras(item):
        if item.quality != 80:
            item.quality = 80

    @staticmethod
    def backstage(item):
        if 10 >= item.sell_in > 5:
            item.quality = item.quality + 2
        elif 5 >= item.sell_in > 0:
            item.quality = item.quality + 3
        elif item.sell_in <= 0:
            item.quality = 0
        else:
            item.quality = item.quality + 1
        item.quality = 50 if item.quality > 50 else item.quality
        item.sell_in = item.sell_in - 1

    @staticmethod
    def conjured(item):
        if item.sell_in > 0:
            item.quality = (item.quality - 2) if item.quality > 2 else 0
            item.sell_in = item.sell_in - 1
        else:
            item.quality = (item.quality - 4) if item.quality > 4 else 0
            item.sell_in = item.sell_in - 1

    def update_quality(self):
        for item in self.items:
            if item.name == "Aged Brie":
                self.aged_brie(item)
            elif item.name == "Sulfuras, Hand of Ragnaros":
                self.sulfuras(item)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                self.backstage(item)
            elif "Conjured" in item.name:
                self.conjured(item)
            else:
                if 50 > item.quality > 0:
                    if item.sell_in <= 0:
                        item.quality = item.quality - 2
                    else:
                        item.quality = item.quality - 1
                item.sell_in = item.sell_in - 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
