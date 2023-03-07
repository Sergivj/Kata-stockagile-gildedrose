from typing import List
from domain.item import Item, BackstagePass, AgedBrie, Sulfuras, Conjured


class Inventory:
    def __init__(self, items: List[Item]):
        self.items = list(items)

    def update_quality(self):
        for item in self.items:
            if "Conjured" in item.name:
                Conjured.calculate_quality(item)
            elif item.name == "Aged Brie":
                AgedBrie.calculate_quality(item)
            elif "Sulfuras" in item.name:
                Sulfuras.calculate_quality(item)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                BackstagePass.calculate_quality(item)
            else:
                if 50 > item.quality > 0:
                    if item.sell_in <= 0:
                        item.quality = item.quality - 2
                    else:
                        item.quality = item.quality - 1
                if item.quality < 0:
                    item.quality = 0
                item.sell_in = item.sell_in - 1
