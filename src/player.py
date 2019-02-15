# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, location):
        self.location = location
        self.inventory = []

    def add_item(self, Item):
        self.inventory.append(Item)

    def xfer_item(self, Item):
        if Item in self.inventory:
            self.inventory.remove(Item)
            return Item
        else:
            print("You don't have one")

    def print_inventory(self):
        inventory_list_string = ""
        for item in self.inventory:
            inventory_list_string += f"** {item.name} - {item.description}\n"

        print(inventory_list_string)
