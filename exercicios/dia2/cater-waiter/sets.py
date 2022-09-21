from cmath import sin
from itertools import count
from operator import index
from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS,
                                  example_dishes,
                                  EXAMPLE_INTERSECTION)

def clean_ingredients(dish_name, dish_ingredients):
    """
    :param dish_name: str
    :param dish_ingredients: list
    :return: tuple of (dish_name, ingredient set)
    This function should return a `tuple` with the name of the dish as the first item,
    followed by the de-duped `set` of ingredients as the second item.
    """
    set_dish_ingredients = set(dish_ingredients)
    
    return (dish_name, set_dish_ingredients)

def check_drinks(drink_name, drink_ingredients):
    """
    :param drink_name: str
    :param drink_ingredients: list
    :return: str drink name + ("Mocktail" or "Cocktail")
    The function should return the name of the drink followed by "Mocktail" if the drink has
    no alcoholic ingredients, and drink name followed by "Cocktail" if the drink includes alcohol.
    """
    count_alcohols_ingredients = 0 
    for ingredient in drink_ingredients:
        if ingredient in ALCOHOLS:
            count_alcohols_ingredients += 1
    
    if count_alcohols_ingredients > 0:
        return f'{drink_name} Cocktail'
    else:
        return f'{drink_name} Mocktail'
    

def categorize_dish(dish_name, dish_ingredients):
    """
    :param dish_name: str
    :param dish_ingredients: list
    :return: str "dish name: CATEGORY"
    This function should return a string with the `dish name: <CATEGORY>` (which meal category the dish belongs to).
    All dishes will "fit" into one of the categories imported from `sets_categories_data.py`
    (VEGAN, VEGETARIAN, PALEO, KETO, or OMNIVORE).
    """
    vegetarian = 0
    vegan = 0 
    paleo = 0
    keto = 0 
    omni = 0 
    for item in dish_ingredients:
        if item in OMNIVORE:
            omni += 1
            omni_list = [omni, "OMNIVORE"]
        if item in PALEO:
            paleo += 1
            paleo_list = [paleo, 'PALEO']
        if item in KETO: 
            keto += 1
            keto_list = [keto, 'KETO']
        if item in VEGETARIAN:
            vegetarian+=1
            vegetarian_list = [vegetarian, 'VEGETARIAN']
        if item in VEGAN:
            vegan +=1
            vegan_list = [vegan, 'VEGAN']
    
    count_ingredients = [omni_list, paleo_list, keto_list, vegetarian_list, vegan_list]

    max_count = max(count_ingredients)
    index_max = count_ingredients.index(max_count)

    return f'{dish_name}: {count_ingredients[index_max][1]}'

def tag_special_ingredients(dish):
    """
    :param dish: tuple of (str of dish name, list of dish ingredients)
    :return: tuple of (str of dish name, set of dish special ingredients)
    Return the dish name followed by the `set` of ingredients that require a special note on the dish description.
    For the purposes of this exercise, all allergens or special ingredients that need to be tracked are in the
    SPECIAL_INGREDIENTS constant imported from `sets_categories_data.py`.
    """

    special_ingredients = []
    for item in dish[1]:
        if item in SPECIAL_INGREDIENTS:
            special_ingredients.append(item)
    
    set_special_ingredients = set(special_ingredients)

    return (dish[0], set_special_ingredients)

def compile_ingredients(dishes):
    """
    :param dishes: list of dish ingredient sets
    :return: set
    This function should return a `set` of all ingredients from all listed dishes.
    """
    ingredients = []
    for cont in range(len(dishes)):
        for item in dishes[cont]:
            ingredients.append(item)

    set_ingredients = set(ingredients)

    return set_ingredients 
    
def separate_appetizers(dishes, appetizers):
    """
    :param dishes: list of dish names
    :param appetizers: list of appetizer names
    :return: list of dish names
    The function should return the list of dish names with appetizer names removed.
    Either list could contain duplicates and may require de-duping.
    """
    set_dishes = set(dishes)
    set_appetizers = set(appetizers)

    dishes = list(set_dishes)

    for item in set_appetizers:
        if item in dishes:
            index_item_dishes = dishes.index(item)
            dishes.pop(index_item_dishes)          
    
    return dishes

def singleton_ingredients(dishes, intersection):
    """
    :param intersection: constant - one of (VEGAN_INTERSECTION,VEGETARIAN_INTERSECTION,PALEO_INTERSECTION,
                                            KETO_INTERSECTION,OMNIVORE_INTERSECTION)
    :param dishes:  list of ingredient sets
    :return: set of singleton ingredients
    Each dish is represented by a `set` of its ingredients.
    Each `<CATEGORY>_INTERSECTION` is an `intersection` of all dishes in the category.
    The function should return a `set` of ingredients that only appear in a single dish.
    """
    list_aux_dishes = []
    list_aux_intersection = []
    singleton = []

    for element in dishes:
        for item in element:
            list_aux_dishes.append(item)
    
    for element in intersection:
        for item in element:
            list_aux_intersection.append(item)

    for item in list_aux_dishes:
        if list_aux_dishes.count(item) == 1:
            singleton.append(item)
    
    for item in list_aux_intersection:
        if item in singleton:
            index = singleton.index(item)
            del singleton[index]

    return singleton


dishestest = [{'water', 'oil'}, {'water', 'sugar', 'butter'}, {'sugar', 'tomato', 'avocado'}]
intersectiontestone = {'sugar', 'avocado'}
intersectiontesttwo = {'butter'}
# print(singleton_ingredients(dishestest, (intersectiontestone,intersectiontesttwo)))
print(singleton_ingredients(example_dishes, EXAMPLE_INTERSECTION))