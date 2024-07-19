# TIC-TAC-TOE

from functools import reduce

def product(l):
    return reduce(lambda a, b: a * b, l)

world = [0] * 9
# world = [0 for i in range(9)] # list comprehension

def print_world(world):
    print('---')
    for y in range(3):
        row = ""
        for x in range(3):
            row += str(world[y * 3 + x])
        print(row)

def won(world):
    # if a row is winner
    # result = world[0] * world[1] * world[2]
    # result = product(world[0:3])
    # world[0:3] == [1] * 3
    for i in range(3):
        result = product(world[i * 3:i * 3 + 3])
        if result == 1:
            return 1
        if result == 8:
            return 2
    # if a column is winner
    # if a diagonal is winner
    
    return 0

print_world(world)
world1 = list(world)
world1[0] = 1
assert won(world1) == 0

world_row_111 = list(world)
world_row_111[0:3] = [1] * 3
assert won(world_row_111) == 1

world_row_222 = list(world)
world_row_222[0:3] = [2] * 3
assert won(world_row_222) == 2

world_row_012 = list(world)
world_row_012[1] = 1
world_row_012[2] = 2
assert won(world_row_012) == 0

world2 = list(world1)
world2[3:6] = [2] * 3
print_world(world2)
assert won(world2) == 2
