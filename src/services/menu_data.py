import csv
from models.dish import Dish
from models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.source_path = source_path
        self.dishes = set()
        self.build_menu()

    def build_menu(self):
        dict_dishes = {}
        with open(self.source_path, "r") as file:
            read_csv = csv.reader(file)
            next(read_csv)

            for each_dich in read_csv:
                dish_name = each_dich[0]
                dish_price = float(each_dich[1])
                ingredient_name = each_dich[2]
                ingredient_amount = int(each_dich[3])
                ingredient_1 = Ingredient(ingredient_name)
                if dish_name not in dict_dishes:
                    new_dish = Dish(dish_name, dish_price)
                    dict_dishes[dish_name] = new_dish
                else:
                    new_dish = dict_dishes[dish_name]

                new_dish.add_ingredient_dependency(
                    ingredient_1, ingredient_amount
                )

            self.dishes = set(dict_dishes.values())


menu_data = MenuData("./data/menu_base_data.csv")
