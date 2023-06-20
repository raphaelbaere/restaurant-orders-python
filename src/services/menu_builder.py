from typing import Dict, List

from services.inventory_control import InventoryMapping
from services.menu_data import MenuData

DATA_PATH = "data/menu_base_data.csv"
INVENTORY_PATH = "data/inventory_base_data.csv"


class MenuBuilder:
    def __init__(self, data_path=DATA_PATH, inventory_path=INVENTORY_PATH):
        self.menu_data = MenuData(data_path)
        self.inventory = InventoryMapping(inventory_path)

    def make_order(self, dish_name: str) -> None:
        try:
            curr_dish = [
                dish
                for dish in self.menu_data.dishes
                if dish.name == dish_name
            ][0]
        except IndexError:
            raise ValueError("Dish does not exist")

        self.inventory.consume_recipe(curr_dish.recipe)

    # Req 4
    def get_main_menu(self, restriction=None) -> List[Dict]:
        self.menu_data = MenuData(DATA_PATH)
        list_of_dicts = []

        for each_dich in self.menu_data.dishes:
            dict_item = {'dish_name': each_dich.name, 'ingredients': each_dich.get_ingredients(), 'price': each_dich.price, 'restrictions': each_dich.get_restrictions()}
            list_of_dicts.append(dict_item)


        def filter_function(each_dich):
            return restriction not in each_dich['restrictions']
        
        return list(filter(filter_function, list_of_dicts))
