from infrastructure.console import ConsoleInventoryRepository, Console
from application.gilded_rose import GildedRose


def main():
    # Construir dependencias
    inventory_repository = ConsoleInventoryRepository()
    gilded_rose = GildedRose(inventory_repository.get_inventory())
    days = 100
    for day in range(days):
        # Mostrar día
        Console().display_day(day)
        # Mostrar salida al usuario
        Console().display_items(gilded_rose.inventory.items)

        # Ejecutar caso de uso
        gilded_rose.update_quality()


if __name__ == "__main__":
    main()
