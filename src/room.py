# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, location, description):
        self.location = location
        self.description = description
        self.items = []

    def __str__(self):
        return f"{self.location}\n{self.description}\n\n"

    # def n_to:
    #     pass #TODO set as a room object or if not set returns an error

    # def s_to:
    #     pass #TODO set as a room object or if not set returns an error

    # def e_to:
    #     pass #TODO set as a room object or if not set returns an error
    #
    # def w_to:
    #     pass #TODO set as a room object or if not set returns an error

    # def items:
    #     pass #TODO create a list of objects in the room
    #
    # def subItem:
    #     pass #TODO handles a player taking an item
    #
    # def addItem:
    #     pass #TODO handles a player dropping an item

