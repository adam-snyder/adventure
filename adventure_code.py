import os
from map import Map

# map (world/location)
size = 10

#OPEN = 0
#WV = 1
#WH = 2
#Q1 = 3
#Q2 = 4
#Q3 = 5
#Q4 = 6

CHARS = [
    '   ',
    ' | ',
    '---',
    ' |-',
    '-| ',
    '-| ',
    ' |-',
]

map = Map()

x = 4
y = 13

# character
inventory = []

def where():
    print(x, y)

# y/n function
def yn(prompt):
    result = input(prompt + ' y/n: ')
    if result == 'y':
        return True
    if result == 'n':
        return False
    return yn(prompt)


# movement function
def move():
    global y
    global x
    result = input('which way would you like to move? (n/s/e/w): ')
    if result == 'n' and map.can_i_move_north(x, y):
        y = y - 1
        return 'you move forward.'
    if result == 's' and map.can_i_move_south(x, y):
        y = y + 1
        return 'you move backward.'
    if result == 'e' and map.can_i_move_east(x, y):
        x = x + 1
        return 'you move to the right.'
    if result == 'w' and map.can_i_move_west(x, y):
        x = x - 1
        return 'you move to the left.'

    print("thats not a direction you can go.")
    return move()


# def can_i_move(xx, yy):
#     print(xx, yy)
#     if xx >= 0 and xx < width and yy >= 0 and yy < height:
#         return world[yy][xx] == 0
#     else:
#         return False
#
# def can_i_move_north():
#     return can_i_move(x, y-1)
#
# def can_i_move_south():
#     return can_i_move(x, y+1)
#
# def can_i_move_east():
#     return can_i_move(x+1, y)
#
# def can_i_move_west():
#     return can_i_move(x-1, y)

# inventory system
def list_items():
    print(inventory)

def add_item(item):
    inventory.append(item)
    print('added ', item, 'to inventory.')

def use_item(item):
    # todo: apply the effects of the item
    inventory.remove(item)
    print('used', item, 'from inventory.')

# test code
map.generate()
map.show(x, y)

#result = yn('do you like cake?')
#print(result)

#where()
while True:
    #os.system('clear')
    result = move()
    print(result)
    map.show(x, y)

#list_items()
#add_item('toilet')
#list_items()
#add_item('plunger')
#list_items()
#use_item('plunger')
#list_items()
