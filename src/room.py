# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, location, description):
        self.location = location
        self.description = description
        self.items = []

    def print_item(self, Item):
        return f"{Item.name} - {Item.description}"

    def __str__(self):
        if len(self.items) > 0:
            item_list_string = "You see:\n"
            for item in self.items:
                item_list_string += f"** {item.name} - {item.description}\n"

        return f"{self.location}\n{self.description}\n{item_list_string}\n"

    def add_item(self, Item):
        self.items.append(Item)

    def xfer_item(self, Item):
        if Item in self.items:
            self.items.remove(Item)
            return Item
        else:
            print("It's not here")
