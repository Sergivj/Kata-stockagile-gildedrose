# -*- coding: utf-8 -*-
import unittest

from application.exceptions import InvalidQualityException
from application.gilded_rose import Item, GildedRose
from infrastructure.console import Console, ConsoleInventoryRepository


class InputText:
    def __init__(self, input_text):
        f = open('../infrastructure/entrada.txt', 'w')
        f.write(input_text)
        f.close()


class GildedRoseTest(unittest.TestCase):
    def test_item_quality_less_0(self):
        """
            Scenario: Item with quality less than 0
            Given a regular item
            When the item is created
            Then raise exception
        """
        items = "+5 Dexterity Vest, 10, -20"
        InputText(items)
        # Construir dependencias
        inventory_repository = ConsoleInventoryRepository()
        with self.assertRaises(InvalidQualityException) as context:
            GildedRose(inventory_repository.get_inventory())
        self.assertTrue('Quality cannot be less than 0' in str(context.exception))

    def test_item_quality_greater_50(self):
        """
            Scenario: Item with quality greater than 50
            Given a regular item
            When the item is created
            Then raise exception
        """
        items = "+5 Dexterity Vest, 10, 60"
        InputText(items)
        # Construir dependencias
        inventory_repository = ConsoleInventoryRepository()
        with self.assertRaises(InvalidQualityException) as context:
            GildedRose(inventory_repository.get_inventory())
        self.assertTrue('Quality cannot be greater than 50' in str(context.exception))

    def test_item_quality_greater_80(self):
        """
            Scenario: Item with quality greater than 80
            Given a regular item
            When the item is created
            Then raise exception
        """
        items = "Sulfuras Hand of Ragnaros, 10, 90"
        InputText(items)
        # Construir dependencias
        inventory_repository = ConsoleInventoryRepository()
        with self.assertRaises(InvalidQualityException) as context:
            GildedRose(inventory_repository.get_inventory())
        self.assertTrue('Quality cannot be greater than 80' in str(context.exception))

    def test_item_regular(self):
        """
            Scenario: Regular item
            Given a regular item
            When the item is updated
            Then the quality and sell_in are decreased
        """
        items = "+5 Dexterity Vest, 10, 20"
        InputText(items)
        # Construir dependencias
        inventory_repository = ConsoleInventoryRepository()
        gilded_rose = GildedRose(inventory_repository.get_inventory())
        gilded_rose.update_quality()
        self.assertEqual("+5 Dexterity Vest, 9, 19", str(gilded_rose.inventory.items[0]))

    def test_item_aged_brie(self):
        """
            Scenario: Aged Brie item
            Given an Aged Brie item
            When the item is updated
            Then the quality increase and sell_in decreases
        """
        items = "Aged Brie, 10, 20"
        InputText(items)
        # Construir dependencias
        inventory_repository = ConsoleInventoryRepository()
        gilded_rose = GildedRose(inventory_repository.get_inventory())
        gilded_rose.update_quality()
        self.assertEqual("Aged Brie, 9, 21", str(gilded_rose.inventory.items[0]))

    def test_item_backstage_pass(self):
        """
            Scenario: Backstage Pass item
            Given a Backstage Pass item
            When the item is updated
            Then the sell_in decreases and quality increases 2 because sell_in is less than 10
        """
        items = "Backstage passes to a TAFKAL80ETC concert, 9, 20"
        InputText(items)
        # Construir dependencias
        inventory_repository = ConsoleInventoryRepository()
        gilded_rose = GildedRose(inventory_repository.get_inventory())
        gilded_rose.update_quality()
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert, 8, 22", str(gilded_rose.inventory.items[0]))

    def test_item_sulfuras(self):
        """
            Scenario: Sulfuras item
            Given a Sulfuras item
            When the item is updated
            Then the item is still the same
        """
        items = "Sulfuras Hand of Ragnaros, 10, 80"
        InputText(items)
        # Construir dependencias
        inventory_repository = ConsoleInventoryRepository()
        gilded_rose = GildedRose(inventory_repository.get_inventory())
        gilded_rose.update_quality()
        self.assertEqual("Sulfuras Hand of Ragnaros, 10, 80", str(gilded_rose.inventory.items[0]))

    def test_item_conjured(self):
        """
            Scenario: Conjured item
            Given a Conjured item
            When the item is updated
            Then the sell_in decreases and quality increase 2
        """
        items = "Conjured Mana Cake, 10, 20"
        InputText(items)
        # Construir dependencias
        inventory_repository = ConsoleInventoryRepository()
        gilded_rose = GildedRose(inventory_repository.get_inventory())
        gilded_rose.update_quality()
        self.assertEqual("Conjured Mana Cake, 9, 18", str(gilded_rose.inventory.items[0]))

    def test_item_conjured_after_sell_in(self):
        """
            Scenario: Conjured item after sell in
            Given a Conjured item
            When the item is updated
            Then the sell_in decreases and quality decrease 4
        """
        items = "Conjured Mana Cake, 0, 20"
        InputText(items)
        # Construir dependencias
        inventory_repository = ConsoleInventoryRepository()
        gilded_rose = GildedRose(inventory_repository.get_inventory())
        gilded_rose.update_quality()
        self.assertEqual("Conjured Mana Cake, -1, 16", str(gilded_rose.inventory.items[0]))

    def test_item_regular_after_sell_in(self):
        """
            Scenario: Regular item after sell in
            Given a regular item
            When the item is updated
            Then the sell_in decreases and quality decrease 2
        """
        items = "+5 Dexterity Vest, 0, 20"
        InputText(items)
        # Construir dependencias
        inventory_repository = ConsoleInventoryRepository()
        gilded_rose = GildedRose(inventory_repository.get_inventory())
        gilded_rose.update_quality()
        self.assertEqual("+5 Dexterity Vest, -1, 18", str(gilded_rose.inventory.items[0]))

    def test_item_aged_brie_after_sell_in(self):
        """
            Scenario: Aged Brie item after sell in
            Given an Aged Brie item
            When the item is updated
            Then the sell_in decreases and quality increase 2
        """
        items = "Aged Brie, 0, 20"
        InputText(items)
        # Construir dependencias
        inventory_repository = ConsoleInventoryRepository()
        gilded_rose = GildedRose(inventory_repository.get_inventory())
        gilded_rose.update_quality()
        self.assertEqual("Aged Brie, -1, 22", str(gilded_rose.inventory.items[0]))

    def test_item_backstage_pass_after_sell_in(self):
        """
            Scenario: Backstage Pass item after sell in
            Given a Backstage Pass item
            When the item is updated
            Then the sell_in decreases and quality is 0 because sell_in is less than 0
        """
        items = "Backstage passes to a TAFKAL80ETC concert, 0, 20"
        InputText(items)
        # Construir dependencias
        inventory_repository = ConsoleInventoryRepository()
        gilded_rose = GildedRose(inventory_repository.get_inventory())
        gilded_rose.update_quality()
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert, -1, 0", str(gilded_rose.inventory.items[0]))

    def test_item_sulfuras_after_sell_in(self):
        """
            Scenario: Sulfuras item after sell in
            Given a Sulfuras item
            When the item is updated
            Then the item is still the same
        """
        items = "Sulfuras Hand of Ragnaros, 0, 80"
        InputText(items)
        # Construir dependencias
        inventory_repository = ConsoleInventoryRepository()
        gilded_rose = GildedRose(inventory_repository.get_inventory())
        gilded_rose.update_quality()
        self.assertEqual("Sulfuras Hand of Ragnaros, 0, 80", str(gilded_rose.inventory.items[0]))

    def test_item_conjured_after_sell_in_and_quality(self):
        """
            Scenario: Conjured item after sell in and quality
            Given a Conjured item
            When the item is updated
            Then the sell_in decreases and quality is 0 because quality dont can be less than 0
        """
        items = "Conjured Mana Cake, 0, 0"
        InputText(items)
        # Construir dependencias
        inventory_repository = ConsoleInventoryRepository()
        gilded_rose = GildedRose(inventory_repository.get_inventory())
        gilded_rose.update_quality()
        self.assertEqual("Conjured Mana Cake, -1, 0", str(gilded_rose.inventory.items[0]))

    def test_item_regular_after_sell_in_and_quality(self):
        """
            Scenario: Regular item after sell in and quality
            Given a regular item
            When the item is updated
            Then the sell_in decreases and quality is 0 because quality dont can be less than 0
        """
        items = "+5 Dexterity Vest, 0, 0"
        InputText(items)
        # Construir dependencias
        inventory_repository = ConsoleInventoryRepository()
        gilded_rose = GildedRose(inventory_repository.get_inventory())
        gilded_rose.update_quality()
        self.assertEqual("+5 Dexterity Vest, -1, 0", str(gilded_rose.inventory.items[0]))

    def test_item_aged_brie_after_sell_in_and_quality(self):
        """
            Scenario: Aged Brie item after sell in and quality
            Given an Aged Brie item
            When the item is updated
            Then the sell_in decreases and quality is 50 because quality dont can be more than 50
        """
        items = "Aged Brie, 0, 50"
        InputText(items)
        # Construir dependencias
        inventory_repository = ConsoleInventoryRepository()
        gilded_rose = GildedRose(inventory_repository.get_inventory())
        gilded_rose.update_quality()
        self.assertEqual("Aged Brie, -1, 50", str(gilded_rose.inventory.items[0]))

    def test_item_backstage_pass_after_sell_in_and_quality(self):
        """
            Scenario: Backstage Pass item after sell in and quality
            Given a Backstage Pass item
            When the item is updated
            Then the sell_in decrease and quality is 0 because sell_in is less than 0
        """
        items = "Backstage passes to a TAFKAL80ETC concert, 0, 50"
        InputText(items)
        # Construir dependencias
        inventory_repository = ConsoleInventoryRepository()
        gilded_rose = GildedRose(inventory_repository.get_inventory())
        gilded_rose.update_quality()
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert, -1, 0", str(gilded_rose.inventory.items[0]))

    def test_item_sulfuras_after_sell_in_and_quality(self):
        """
            Scenario: Sulfuras item after sell in and quality
            Given a Sulfuras item
            When the item is updated
            Then the item is still the same
        """
        items = "Sulfuras Hand of Ragnaros, 0, 80"
        InputText(items)
        # Construir dependencias
        inventory_repository = ConsoleInventoryRepository()
        gilded_rose = GildedRose(inventory_repository.get_inventory())
        gilded_rose.update_quality()
        self.assertEqual("Sulfuras Hand of Ragnaros, 0, 80", str(gilded_rose.inventory.items[0]))


if __name__ == '__main__':
    unittest.main()
