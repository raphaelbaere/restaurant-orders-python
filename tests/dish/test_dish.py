from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient
import pytest

# Req 2
def test_dish():
    dish = Dish("hamburguer", 25.00)
    dish2 = Dish("hamburguer", 25.00)
    dish3 = Dish("lasagna", 35.00)

    assert dish.name == "hamburguer"
    assert dish.price == 25.00


    with pytest.raises(TypeError):
        Dish("hamburguer", "25")
    with pytest.raises(ValueError):
        Dish("hamburguer", 0)

    
    assert dish.__eq__(dish2) is True
    assert dish.__eq__(dish3) is False
    assert dish.__hash__() == dish2.__hash__()
    assert dish.__hash__() != dish3.__hash__()
    assert dish.__repr__() == f"Dish('{dish.name}', R${dish.price:.2f})"

    ingr1 = Ingredient("queijo mussarela")
    ingr2 = Ingredient("presunto")
    dish.add_ingredient_dependency(ingr1, 2)
    dish.add_ingredient_dependency(ingr2, 2)
    assert dish.recipe.get(ingr1) == 2
    assert dish.recipe.get(ingr2) == 2

    assert dish.get_restrictions() == ingr1.restrictions.union(
        ingr2.restrictions
    )