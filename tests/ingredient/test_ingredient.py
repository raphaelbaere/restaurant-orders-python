from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    presunto = Ingredient("Presunto")
    queijo = Ingredient("Queijo")
    assert presunto.__eq__(queijo) is False
    assert presunto.__eq__(presunto) is True
    assert presunto.__hash__() != queijo.__hash__()
    assert presunto.__hash__() == presunto.__hash__()
    assert presunto.name == "Presunto"
    assert presunto.__repr__() == f"Ingredient('{presunto.name}')"
    assert presunto.restrictions == set()
