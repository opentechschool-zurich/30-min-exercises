# TIC-TAC-TOE

from functools import reduce

def product(l):
    return reduce(lambda a, b: a * b, l)

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
    for column in range(3):
        # result = product(world[column * 3:column * 3 + 3])
        # 0 1 2
        # 3 4 5
        # 6 7 8
        result = world[0 + column] * world[3 + column] * world[6 + column]
        if result == 1:
            return 1
        if result == 8:
            return 2
    # if a diagonal is winner
  
    result = world[0] * world[4] * world[8]
    if result == 1:
        return 1
    if result == 8:
        return 2
    result = world[2] * world[4] * world[6]
    if result == 1:
        return 1
    if result == 8:
        return 2

    return 0

def main():
    world = [0] * 9
    # world = [0 for i in range(9)] # list comprehension


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

    world_column_1_1 = list(world)
    world_column_1_1[0] = 1
    world_column_1_1[3] = 1
    world_column_1_1[6] = 1

    assert won(world_column_1_1) == 1

    world_column_2_2 = list(world)
    world_column_2_2[1] = 2
    world_column_2_2[4] = 2
    world_column_2_2[7] = 2

    assert won(world_column_2_2) == 2

    world_column_0_0 = list(world)
    world_column_0_0[0] = 1
    world_column_0_0[4] = 1
    assert won(world_column_0_0) == 0

    diagonal = list(world)
    diagonal[0] = 1
    diagonal[4] = 1
    diagonal[8] = 1
    assert won(diagonal) == 1

    diagonal = list(world)
    diagonal[0] = 2
    diagonal[4] = 2
    diagonal[8] = 2
    assert won(diagonal) == 2

    diagonal = list(world)
    diagonal[2] = 1
    diagonal[4] = 1
    diagonal[6] = 1
    assert won(diagonal) == 1

    diagonal = list(world)
    diagonal[2] = 2
    diagonal[4] = 2
    diagonal[6] = 2
    assert won(diagonal) == 2

if __name__ == '__main__':
    main()
