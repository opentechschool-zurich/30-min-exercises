def move(towers, source, target):
    towers[target].append(towers[source].pop())

def get_smallest_pole(towers):
    smallest = None
    for key, values in enumerate(towers):
        if len(values) == 0:
            continue
        elif smallest == None:
            smallest = key
        elif values[-1] < towers[smallest][-1]:
            smallest = key
    return smallest

def solved(towers, discs_count):
    return len(towers[2]) == discs_count

def solve(towers):

    discs_count = len(towers[0])
    direction = 1 if  discs_count % 2 == 0 else -1

    while True:
        # A simple solution for the toy puzzle is to alternate moves between the smallest piece
        # and a non-smallest piece.
        source = get_smallest_pole(towers)
        # When moving the smallest piece, always move it to the next position in the same direction
        # (to the right if the starting number of pieces is even, to the left if the starting number of pieces is odd).
        # If there is no tower position in the chosen direction, move the piece to the opposite end, but then continue to move in the correct direction.
        target = (source + direction) % 3
        other = (source - direction) % 3
        print(source, target, other)
        move(towers, source, target)
        if solved(towers, discs_count):
            return
        print(towers)
        # When the turn is to move the non-smallest piece, there is only one legal move.
        if len(towers[source]) == 0:
            move(towers, other, source)
        elif len(towers[other]) == 0:
            move(towers, source, other)
        elif towers[source][-1] < towers[other][-1]:
            move(towers, source, other)
        else:
            move(towers, other, source)
        if solved(towers, discs_count):
            return
        print(towers)

def main():
    towers = [
        [2, 1, 0],
        [],
        []
    ]
    print(towers)
    # move(towers, 0, 2)
    # print(towers)
    # move(towers, 0, 1)
    # print(towers)
    # move(towers, 2, 1)
    # print(towers)
    # move(towers, 0, 2)
    # print(towers)
    # move(towers, 1, 0)
    # print(towers)
    # move(towers, 1, 2)
    # print(towers)
    # move(towers, 0, 2)
    solve(towers)
    print(towers)

if __name__ == '__main__':
    main()
