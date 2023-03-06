# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_regular_item(self):
        """
            Scenario: Regular item
            Given a regular item
            When the item is updated
            Then the quality decreases by 1
            And the sell_in decreases by 1
        """
        items = [Item(name="+5 Dexterity Vest", sell_in=10, quality=20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 19)
        self.assertEqual(items[0].sell_in, 9)

    def test_regular_item_after_sell_in(self):
        """
            Scenario: Regular item after sell_in
            Given a regular item
            When the item is updated
            Then the quality decreases by 2
            And the sell_in decreases by 1
        """
        items = [Item(name="+5 Dexterity Vest", sell_in=0, quality=20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 18)
        self.assertEqual(items[0].sell_in, -1)

    def test_regular_item_quality_zero(self):
        """
            Scenario: Regular item quality zero
            Given a regular item
            When the item is updated
            Then the quality is 0
            And the sell_in decreases by 1
        """
        items = [Item(name="+5 Dexterity Vest", sell_in=0, quality=0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 0)
        self.assertEqual(items[0].sell_in, -1)

    def test_aged_brie(self):
        """
            Scenario: Aged Brie
            Given an Aged Brie item
            When the item is updated
            Then the quality increases by 1
            And the sell_in decreases by 1
        """
        items = [Item(name="Aged Brie", sell_in=2, quality=0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 1)
        self.assertEqual(items[0].sell_in, 1)

    def test_aged_brie_quality_50(self):
        """
            Scenario: Aged Brie quality 50
            Given an Aged Brie item
            When the item is updated
            Then the quality is 50
            And the sell_in decreases by 1
        """
        items = [Item(name="Aged Brie", sell_in=2, quality=50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 50)
        self.assertEqual(items[0].sell_in, 1)

    def test_sulfuras(self):
        """
            Scenario: Sulfuras
            Given a Sulfuras item
            When the item is updated
            Then the quality is 80
            And the sell_in is 0
        """
        items = [Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 80)
        self.assertEqual(items[0].sell_in, 0)

    def test_backstage_passes(self):
        """
            Scenario: Backstage passes
            Given a Backstage passes item
            When the item is updated
            Then the quality increases by 1
            And the sell_in decreases by 1
        """
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 21)
        self.assertEqual(items[0].sell_in, 14)

    def test_backstage_passes_10_days(self):
        """
            Scenario: Backstage passes 10 days
            Given a Backstage passes item
            When the item is updated
            Then the quality increases by 2
            And the sell_in decreases by 1
        """
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 22)
        self.assertEqual(items[0].sell_in, 9)

    def test_backstage_passes_5_days(self):
        """
            Scenario: Backstage passes 5 days
            Given a Backstage passes item
            When the item is updated
            Then the quality increases by 3
            And the sell_in decreases by 1
        """
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 23)
        self.assertEqual(items[0].sell_in, 4)

    def test_backstage_passes_after_sell_in(self):
        """
            Scenario: Backstage passes after sell_in
            Given a Backstage passes item
            When the item is updated
            Then the quality is 0
            And the sell_in decreases by 1
        """
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 0)
        self.assertEqual(items[0].sell_in, -1)

    def test_conjured_item(self):
        """
            Scenario: Conjured item
            Given a Conjured item
            When the item is updated
            Then the quality decreases by 2
            And the sell_in decreases by 1
        """
        items = [Item(name="Conjured Mana Cake", sell_in=3, quality=6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 4)
        self.assertEqual(items[0].sell_in, 2)

    def test_conjured_item_after_sell_in(self):
        """
            Scenario: Conjured item after sell_in
            Given a Conjured item
            When the item is updated
            Then the quality decreases by 4
            And the sell_in decreases by 1
        """
        items = [Item(name="Conjured Mana Cake", sell_in=0, quality=6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 2)
        self.assertEqual(items[0].sell_in, -1)

    def test_conjured_item_quality_zero(self):
        """
            Scenario: Conjured item quality zero
            Given a Conjured item
            When the item is updated
            Then the quality is 0
            And the sell_in decreases by 1
        """
        items = [Item(name="Conjured Mana Cake", sell_in=3, quality=0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 0)
        self.assertEqual(items[0].sell_in, 2)

    def test_conjured_item_quality_zero_after_sell_in(self):
        """
            Scenario: Conjured item quality zero after sell_in
            Given a Conjured item
            When the item is updated
            Then the quality is 0
            And the sell_in decreases by 1
        """
        items = [Item(name="Conjured Mana Cake", sell_in=0, quality=0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 0)
        self.assertEqual(items[0].sell_in, -1)

    def test_conjured_item_quality_50(self):
        """
            Scenario: Conjured item quality 50
            Given a Conjured item
            When the item is updated
            Then the quality is 48
            And the sell_in decreases by 1
        """
        items = [Item(name="Conjured Mana Cake", sell_in=3, quality=50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 48)
        self.assertEqual(items[0].sell_in, 2)

    def test_conjured_item_quality_50_after_sell_in(self):
        """
            Scenario: Conjured item quality 50 after sell_in
            Given a Conjured item
            When the item is updated
            Then the quality is 46
            And the sell_in decreases by 1
        """
        items = [Item(name="Conjured Mana Cake", sell_in=0, quality=50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 46)
        self.assertEqual(items[0].sell_in, -1)

    def test_conjured_item_quality_49(self):
        """
            Scenario: Conjured item quality 49
            Given a Conjured item
            When the item is updated
            Then the quality is 47
            And the sell_in decreases by 1
        """
        items = [Item(name="Conjured Mana Cake", sell_in=3, quality=49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 47)
        self.assertEqual(items[0].sell_in, 2)

    def test_conjured_item_quality_49_after_sell_in(self):
        """
            Scenario: Conjured item quality 49 after sell_in
            Given a Conjured item
            When the item is updated
            Then the quality is 45
            And the sell_in decreases by 1
        """
        items = [Item(name="Conjured Mana Cake", sell_in=0, quality=49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 45)
        self.assertEqual(items[0].sell_in, -1)

    def test_conjured_item_quality_1(self):
        """
            Scenario: Conjured item quality 1
            Given a Conjured item
            When the item is updated
            Then the quality is 0
            And the sell_in decreases by 1
        """
        items = [Item(name="Conjured Mana Cake", sell_in=3, quality=1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 0)
        self.assertEqual(items[0].sell_in, 2)

    def test_conjured_item_quality_1_after_sell_in(self):
        """
            Scenario: Conjured item quality 1 after sell_in
            Given a Conjured item
            When the item is updated
            Then the quality is 0
            And the sell_in decreases by 1
        """
        items = [Item(name="Conjured Mana Cake", sell_in=0, quality=1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 0)
        self.assertEqual(items[0].sell_in, -1)

    def test_conjured_item_quality_2(self):
        """
            Scenario: Conjured item quality 2
            Given a Conjured item
            When the item is updated
            Then the quality is 0
            And the sell_in decreases by 1
        """
        items = [Item(name="Conjured Mana Cake", sell_in=3, quality=2)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 0)
        self.assertEqual(items[0].sell_in, 2)

    def test_conjured_item_quality_2_after_sell_in(self):
        """
            Scenario: Conjured item quality 2 after sell_in
            Given a Conjured item
            When the item is updated
            Then the quality is 0
            And the sell_in decreases by 1
        """
        items = [Item(name="Conjured Mana Cake", sell_in=0, quality=2)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 0)
        self.assertEqual(items[0].sell_in, -1)

    def test_conjured_item_quality_3(self):
        """
            Scenario: Conjured item quality 3
            Given a Conjured item
            When the item is updated
            Then the quality is 1
            And the sell_in decreases by 1
        """
        items = [Item(name="Conjured Mana Cake", sell_in=3, quality=3)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 1)
        self.assertEqual(items[0].sell_in, 2)

    def test_conjured_item_quality_3_after_sell_in(self):
        """
            Scenario: Conjured item quality 3 after sell_in
            Given a Conjured item
            When the item is updated
            Then the quality is 0
            And the sell_in decreases by 1
        """
        items = [Item(name="Conjured Mana Cake", sell_in=0, quality=3)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 0)
        self.assertEqual(items[0].sell_in, -1)

    def test_conjured_item_quality_4(self):
        """
            Scenario: Conjured item quality 4
            Given a Conjured item
            When the item is updated
            Then the quality is 2
            And the sell_in decreases by 1
        """
        items = [Item(name="Conjured Mana Cake", sell_in=3, quality=4)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 2)
        self.assertEqual(items[0].sell_in, 2)

    def test_conjured_item_quality_4_after_sell_in(self):
        """
            Scenario: Conjured item quality 4 after sell_in
            Given a Conjured item
            When the item is updated
            Then the quality is 0
            And the sell_in decreases by 1
        """
        items = [Item(name="Conjured Mana Cake", sell_in=0, quality=4)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 0)
        self.assertEqual(items[0].sell_in, -1)

    def test_conjured_item_quality_5(self):
        """
            Scenario: Conjured item quality 5
            Given a Conjured item
            When the item is updated
            Then the quality is 3
            And the sell_in decreases by 1
        """
        items = [Item(name="Conjured Mana Cake", sell_in=3, quality=5)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 3)
        self.assertEqual(items[0].sell_in, 2)

    def test_conjured_item_quality_5_after_sell_in(self):
        """
            Scenario: Conjured item quality 5 after sell_in
            Given a Conjured item
            When the item is updated
            Then the quality is 1
            And the sell_in decreases by 1
        """
        items = [Item(name="Conjured Mana Cake", sell_in=0, quality=5)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 1)
        self.assertEqual(items[0].sell_in, -1)

    def test_conjured_item_quality_6(self):
        """
            Scenario: Conjured item quality 6
            Given a Conjured item
            When the item is updated
            Then the quality is 4
            And the sell_in decreases by 1
        """
        items = [Item(name="Conjured Mana Cake", sell_in=3, quality=6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 4)
        self.assertEqual(items[0].sell_in, 2)

    def test_conjured_item_quality_6_after_sell_in(self):
        """
            Scenario: Conjured item quality 6 after sell_in
            Given a Conjured item
            When the item is updated
            Then the quality is 2
            And the sell_in decreases by 1
        """
        items = [Item(name="Conjured Mana Cake", sell_in=0, quality=6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 2)
        self.assertEqual(items[0].sell_in, -1)

    def test_conjured_item_quality_7(self):
        """
            Scenario: Conjured item quality 7
            Given a Conjured item
            When the item is updated
            Then the quality is 5
            And the sell_in decreases by 1
        """
        items = [Item(name="Conjured Mana Cake", sell_in=3, quality=7)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 5)
        self.assertEqual(items[0].sell_in, 2)

    def test_conjured_item_quality_7_after_sell_in(self):
        """
            Scenario: Conjured item quality 7 after sell_in
            Given a Conjured item
            When the item is updated
            Then the quality is 3
            And the sell_in decreases by 1
        """
        items = [Item(name="Conjured Mana Cake", sell_in=0, quality=7)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 3)
        self.assertEqual(items[0].sell_in, -1)


if __name__ == '__main__':
    unittest.main()
