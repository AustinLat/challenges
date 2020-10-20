# Having home and contents insurance requires you to accurately indicate the value of the items in your house. The idea
# came to me when doing this for myself.
# What if I could write a simple program that allowed me to create a list of rooms in my house and for each room a list
# of items along with their dollar values?
# House Inventory Tracker Requirements
#     Create a list of rooms (doesn't have to use the list type).
#     Each room in your rooms list needs to contain at least 5 items (ie, TV, couch, table, etc) and the relative dollar
#     value of each item.
#     The script you will write will print out each room along with the individual items and values. This needs to be
#     properly formatted, eg: no printing a dict as is.
#
# Bonus
# These are bonus features. Not required but cool to try if you're interested:
#     Create some sort of program shell with a menu system around this. ie, "Which room would you like to list out?"
#     If you're really game, allow users to create rooms and update information.
#     You could even make an API with Flask or your preferred framework
#     Print the total dollar value of each room and the entire house.
#     Have persistent storage of the data. sqlite3 = stdlib and light-weight, but feel free to use your preferred
#     DB / module.



def insuredItems():
    bedroom = {'bed': 1000, 'desk': 200, 'computer': 2000, 'lamp': 60, 'TV': 1000}
    living_room = {'couch': 2000, 'TV': 2000, 'table': 500, 'coffee_table': 400, 'rugs': 20000}
    rooms = [bedroom, living_room]
    for room in rooms:
        for item in room:
            print(f'({item} is {room[item]} dollars)')

def addItems():
    room = input('Please enter room name: ')
    item = input('Please enter item name: ')
    price = input('Please enter price: ')


insuredItems()