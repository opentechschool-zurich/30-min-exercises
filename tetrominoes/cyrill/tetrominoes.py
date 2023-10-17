L = [
    [0, 1, 0],
    [0, 1, 0],
    [1, 1, 0]
]

T = [
    [1, 1, 1],
    [0, 1, 0],
    [0, 0, 0]
]

Z = [
    [0, 0, 1],
    [0, 1, 1],
    [0, 1, 0]
]

def rotate(piece):
    result = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    for x in range(0, 3):
        for y in range(0, 3):
            result[2 - y][x] = piece[x][y]
    return result

print(repr(L))
print(repr(rotate(L)))
print(repr(rotate(rotate(L))))
print(repr(rotate(rotate(rotate(L)))))
