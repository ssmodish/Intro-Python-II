from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

item = {
    'excalibur': Item("Excalibur",
                      "A really nice sword"),

    'rusty': Item("A rusty fork",
                  "You might be able to shine it up"),

    'old_clothes': Item("Some old clothes",
                        "You had no idea what you were doing today, did you?")
}


room['overlook'].add_item(item['excalibur'])
room['overlook'].add_item(item['rusty'])

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'])
player.add_item(item['old_clothes'])


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


directional_error_message = '\n--- YOU CAN NOT WALK THROUGH WALLS!!!!! ---\n'
directions = 'Choose n, s, e, or w'

# player.location = room[player.location].n_to.location.lower()
#
print(player.location)

action_sequence = []


def inputAction():
    action_sequence = input("What are you going to do?\n").lower().split()
    if len(action_sequence) > 1:
        # two word command
        active_item_name = action_sequence[1]
        action_name = action_sequence[0]

        # get or drop?
        if action_name == 'get':
            player.add_item(player.location.xfer_item(item[active_item_name]))
        elif action_name == 'drop':
            player.location.add_item(player.xfer_item((item[active_item_name])))

    return action_sequence[0]

action = inputAction()



print(action)

# *** MAIN GAME LOOP ***
while action != 'q':
    if action == 'n':
        if hasattr(player.location, 'n_to'):
            player.location = player.location.n_to
        else:
            print(directional_error_message)

    elif action == 's':
        if hasattr(player.location, 's_to'):
            player.location = player.location.s_to
        else:
            print(directional_error_message)

    elif action == 'e':
        if hasattr(player.location, 'e_to'):
            player.location = player.location.e_to
        else:
            print(directional_error_message)

    elif action == 'w':
        if hasattr(player.location, 'w_to'):
            player.location = player.location.w_to
        else:
            print(directional_error_message)
    elif action == 'i':
        player.print_inventory()

    print(player.location)
    print(directions)
    action = inputAction()
