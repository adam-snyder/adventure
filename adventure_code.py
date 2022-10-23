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

height = 0
width = 0
world = []

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
    if result == 'n' and can_i_move_north():
        y = y - 1
        return 'you move forward.'
    if result == 's' and can_i_move_south():
        y = y + 1
        return 'you move backward.'
    if result == 'e' and can_i_move_east():
        x = x + 1
        return 'you move to the right.'
    if result == 'w' and can_i_move_west():
        x = x - 1
        return 'you move to the left.'

    print("thats not a direction you can go.")
    return move()

def make_map():
    global width
    global world
    global height
    world = ([
        [ 0, 6, 2, 2, 2, 2, 2, 5, 0, 0 ],
        [ 0, 1, 0, 0, 0, 0, 0, 1, 0, 0 ],
        [ 0, 1, 0, 6, 2, 5, 0, 1, 0, 0 ],
        [ 0, 1, 0, 1, 0, 1, 0, 1, 0, 0 ],
        [ 0, 1, 0, 1, 0, 1, 0, 3, 2, 5 ],
        [ 0, 1, 0, 1, 0, 1, 0, 0, 0, 1 ],
        [ 0, 1, 0, 1, 0, 3, 2, 5, 0, 1 ],
        [ 0, 1, 0, 1, 0, 0, 0, 1, 0, 1 ],
        [ 6, 4, 0, 3, 2, 5, 0, 1, 0, 1 ],
        [ 1, 0, 0, 0, 0, 1, 0, 1, 0, 1 ],
        [ 1, 0, 6, 5, 0, 1, 0, 1, 0, 1 ],
        [ 1, 0, 1, 1, 0, 1, 0, 1, 0, 1 ],
        [ 3, 2, 4, 1, 0, 1, 0, 1, 0, 1 ],
        [ 0, 0, 0, 1, 0, 1, 0, 1, 0, 1 ],
    ])
    height = len(world)
    width = len(world[0])

def show_map():
    print(f'{width} x {height} map')
    for yy in range(height):
        line = []
        for xx in range(width):
            symbol = CHARS[world[yy][xx]]
            if yy == y and xx == x:
                symbol = ' * '
            line.append(symbol)
        print(' '.join(line))
    print('\n')

def can_i_move(xx, yy):
    print(xx, yy)
    if xx >= 0 and xx < width and yy >= 0 and yy < height:
        return world[yy][xx] == 0
    else:
        return False

def can_i_move_north():
    return can_i_move(x, y-1)

def can_i_move_south():
    return can_i_move(x, y+1)

def can_i_move_east():
    return can_i_move(x+1, y)

def can_i_move_west():
    return can_i_move(x-1, y)


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
make_map()
show_map()

#result = yn('do you like cake?')
#print(result)

#where()
while True:
    result = move()
    print(result)
    show_map()

#list_items()
#add_item('toilet')
#list_items()
#add_item('plunger')
#list_items()
#use_item('plunger')
#list_items()
