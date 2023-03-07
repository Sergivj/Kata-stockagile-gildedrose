from domain.item import Item, BackstagePass, AgedBrie, Sulfuras, Conjured
from domain.inventory import Inventory
from application.exceptions import InvalidQualityException


class GildedRose:
    def __init__(self, items):
        self.inventory = Inventory(items)

    def update_quality(self):
        self.inventory.update_quality()


def check_quality(quality, sulfuras=False):
    try:
        if quality > 50 and not sulfuras:
            raise InvalidQualityException("Quality cannot be greater than 50")
        elif quality < 0:
            raise InvalidQualityException("Quality cannot be less than 0")
        elif quality > 80:
            raise InvalidQualityException("Quality cannot be greater than 80")
    except InvalidQualityException as e:
        raise InvalidQualityException(e.message)


class ItemFactory:
    @staticmethod
    def create_item(name: str, sell_in: int, quality: int) -> Item:
        if "Conjured" in name:
            check_quality(quality, sulfuras=True) if "Sulfuras" in name else check_quality(quality, sulfuras=False)
            return Conjured(name, sell_in, quality)
        if name == "Backstage passes to a TAFKAL80ETC concert":
            check_quality(quality, sulfuras=False)
            return BackstagePass(name, sell_in, quality)
        elif name == "Aged Brie":
            check_quality(quality, sulfuras=False)
            return AgedBrie(name, sell_in, quality)
        elif "Sulfuras" in name:
            check_quality(quality, sulfuras=True)
            return Sulfuras(name, sell_in, quality)
        else:
            check_quality(quality, sulfuras=False)
            return Item(name, sell_in, quality)
