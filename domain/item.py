
class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def check_max_quality(self):
        if self.quality > 50:
            self.quality = 50

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class BackstagePass(Item):
    def calculate_quality(self):
        if 10 >= self.sell_in > 5:
            self.quality = self.quality + 2
        elif 5 >= self.sell_in > 0:
            self.quality = self.quality + 3
        elif self.sell_in <= 0:
            self.quality = 0
        else:
            self.quality = self.quality + 1
        self.check_max_quality()
        self.sell_in = self.sell_in - 1


class AgedBrie(Item):
    def calculate_quality(self):
        if self.quality < 50:
            self.quality = self.quality + 1
        if self.sell_in <= 0:
            self.quality = self.quality + 1
        self.sell_in = self.sell_in - 1
        self.check_max_quality()


class Sulfuras(Item):
    def calculate_quality(self):
        if self.quality != 80:
            self.quality = 80


class Conjured(Item):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)
        self.multiplier = 2

    def calculate_quality(self):
        if "Aged Brie" in self.name:
            for _ in range(self.multiplier):
                AgedBrie.calculate_quality(self)
                self.sell_in += 1
            self.sell_in -= 1
        elif "Sulfuras" in self.name:
            for _ in range(self.multiplier):
                Sulfuras.calculate_quality(self)
        elif "Backstage passes to a TAFKAL80ETC concert" in self.name:
            for _ in range(self.multiplier):
                BackstagePass.calculate_quality(self)
                self.sell_in += 1
            self.sell_in -= 1
        else:
            if self.sell_in > 0:
                self.quality = (self.quality - 2) if self.quality > 2 else 0
                self.sell_in = self.sell_in - 1
            else:
                self.quality = (self.quality - 4) if self.quality > 4 else 0
                self.sell_in = self.sell_in - 1
