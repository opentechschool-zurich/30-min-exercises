# TIC-TAC-TOE

def print_world(world):
    print('---')
    for y in range(3):
        row = ""
        for x in range(3):
            row += str(world[y * 3 + x])
        print(row)

PLAYER_1_WON_PRODUCT  = 1
PLAYER_2_WON_PRODUCT  = 8
TOP_LEFT = 0
TOP_MIDDLE = 1
TOP_RIGHT = 2
MIDDLE_LEFT = 3
MIDDLE_MIDDLE = 4
MIDDLE_RIGHT = 5
BOTTOM_LEFT = 6
BOTTOM_MIDDLE = 7
BOTTOM_RIGHT = 8

def won(world):
    to_be_checked = [
        [TOP_LEFT, TOP_MIDDLE, TOP_RIGHT], # rows
        [MIDDLE_LEFT, MIDDLE_MIDDLE, MIDDLE_RIGHT],
        [BOTTOM_LEFT, BOTTOM_MIDDLE, BOTTOM_RIGHT],
        [TOP_LEFT, MIDDLE_LEFT, BOTTOM_LEFT], # columns
        [TOP_MIDDLE, MIDDLE_MIDDLE, BOTTOM_MIDDLE],
        [TOP_RIGHT, MIDDLE_RIGHT, BOTTOM_RIGHT],
        [TOP_LEFT, MIDDLE_MIDDLE, BOTTOM_RIGHT], # both diagonals
        [TOP_RIGHT, MIDDLE_MIDDLE, BOTTOM_LEFT]
    ]
    # for [a, b, c] in to_be_checked:
    #     result = world[a] * world[b] * world[c]
    for triple in to_be_checked:
        result = world[triple[0]] * world[triple[1]] * world[triple[2]]
        if result == PLAYER_1_WON_PRODUCT:
            return 1
        elif result == PLAYER_2_WON_PRODUCT:
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
