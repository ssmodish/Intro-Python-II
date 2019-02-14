from room import Room
from player import Player

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



#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player('outside')

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


directional_error_message = 'You can not walk through walls!'
directions = 'Choose n, s, e, or w'

print(room[player.location])
# player.location = room[player.location].n_to.location.lower()
#
# print(room[player.location])

action = input()


while action != 'q':
    if action == 'n':
        if hasattr(room[player.location], 'n_to'):
            player.location = room[player.location].n_to.location.lower().split()[0]
        else:
            print(directional_error_message);

    elif action == 's':
        if hasattr(room[player.location], 's_to'):
            player.location = room[player.location].s_to.location.lower().split()[0]
        else:
            print(directional_error_message);

    elif action == 'e':
        if hasattr(room[player.location], 'e_to'):
            player.location = room[player.location].e_to.location.lower().split()[0]
        else:
            print(directional_error_message);

    elif action == 'w':
        if hasattr(room[player.location], 'w_to'):
            player.location = room[player.location].w_to.location.lower().split()[0]
        else:
            print(directional_error_message);

    print(room[player.location])
    print(directions)
    action = input()
