from xml.dom.minidom import Element


def create_inventory(items):
    """
    :param items: list - list of items to create an inventory from.
    :return:  dict - the inventory dictionary.
    """
    inventory_list = []
    for element in items:
        count_item = items.count(element)
        items_quantity = (element, count_item)
        if items_quantity not in inventory_list:
            inventory_list.append(items_quantity)
    
    return dict(inventory_list)
          
def add_items(inventory, items):
    """
    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return:  dict - the inventory dictionary update with the new items.
    """
    dict_add = create_inventory(items) 
    for element in dict_add:
        if element in inventory:
            inventory[element] += dict_add[element]
        else:
            inventory[element] = dict_add[element]
    
    return inventory

def decrement_items(inventory, items):
    """
    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return:  dict - updated inventory dictionary with items decremented.
    """
    for element in items:
        if (element in inventory) and ( inventory[element] > 0):
            inventory[element] -= 1
    
    return inventory

def remove_item(inventory, item):
    """
    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return:  dict - updated inventory dictionary with item removed.
    """
    if item in inventory:
        del inventory[item]

    return inventory

def list_inventory(inventory):
    """
    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    list_tuple_inventory = []
    for item in inventory:
        if inventory[item] > 0:
            list_tuple_inventory.append((item, inventory[item]))
    
    return list_tuple_inventory
