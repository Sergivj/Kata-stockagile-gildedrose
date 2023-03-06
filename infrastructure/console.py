from typing import List

from application.gilded_rose import ItemFactory
from application.gilded_rose import Item


class Console:
    @staticmethod
    def get_user_input() -> List[str]:
        # Lógica para obtener los datos de entrada del usuario a través de la consola
        input_data = []
        try:
            with open('infrastructure/entrada.txt') as f:
                for line in f:
                    input_data.append(line)
        except:
            with open('../infrastructure/entrada.txt') as f:
                for line in f:
                    input_data.append(line)
        return input_data

    @staticmethod
    def display_items(items):
        # Lógica para mostrar los datos de salida al usuario a través de la consola
        for item in items:
            print(item)

    @staticmethod
    def display_day(day):
        # Lógica para mostrar el día al usuario a través de la consola
        print("")
        print("-------- day %s --------" % day)


class ConsoleInventoryRepository:
    @staticmethod
    def get_inventory() -> List[Item]:
        items = []
        if Console().get_user_input() is None:
            return []

        for data in Console().get_user_input():
            name, sell_in, quality = data.split(",")
            item = ItemFactory.create_item(name=name, sell_in=int(sell_in), quality=int(quality))
            items.append(item)
        return items
