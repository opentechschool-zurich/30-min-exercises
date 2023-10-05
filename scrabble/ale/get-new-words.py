import sys
from dataclasses import dataclass

# TODO: support "parallel" words

@dataclass
class Tile:
    letter: str
    x: int
    y: int

def sort_tiles(tiles):
    return tiles.sort(key=lambda k: [k.y, k.x])

def exists(board, letter_added, direction):
    if letter_added.x + direction[0] < 0 or letter_added.x + direction[0] > len(board[0]) - 1:
        return False
    if letter_added.y + direction[1] < 0 or letter_added.y + direction[1] > len(board) - 1:
        return False
    if board[letter_added.x + direction[0]][letter_added.y + direction[1]] == '':
        return False
    return True

def get_row(board, y):
    """ return a copy of the row y """
    return [Tile(c, x, y) for x, c in enumerate(board[y])]

def get_column(board, x):
    """ return a copy of the column x """
    return [Tile(row[x], x, y)  for y, row in enumerate(board)]

def get_horizontal_word(board, tiles):    
    result = []
    row = get_row(board, tiles[0].y)
    for tile in tiles:
        row[tile.x] = tile
    # print(f'row: {row}')
    for tile in reversed(row[0:tiles[0].x]):
        if tile.letter == '':
            break
        result.insert(0, tile)
    result.append(tiles[0])
    # print(f'result: {result}')
    for tile in row[tiles[0].x + 1:]:
        # print(f'>{tile.letter}:{tile.x}')
        if tile.letter == '':
            break
        result.append(tile)
    return result

def get_vertical_word(board, tiles):
    result = []
    # print(board)
    column = get_column(board, tiles[0].x)
    for tile in tiles:
        column[tile.y] = tile
    # print(f'column: {column}')
    for tile in reversed(column[0:tiles[0].y]):
        # print(f'<{tile}:{tile.y - y}')
        if tile.letter == '':
            break
        result.insert(0, tile)
    result.append(tiles[0])
    # print(f'result: {result}')
    for tile in column[tiles[0].y + 1:]:
        # print(f'>{tile.letter}:{tile.y}')
        if tile.letter == '':
            break
        result.append(tile)
    return result

def get_words_for_new_tiles(board, tiles_added):
    words = []
    # print(tiles_added)
    #
    sort_tiles(tiles_added)

    tiles_horizontal = True
    tiles_vertical = True
    if len(tiles_added) > 1:
        tiles_horizontal = tiles_added[0].y == tiles_added[1].y
        tiles_vertical = tiles_added[0].x == tiles_added[1].x
    # print(tiles_added)
    # print(tiles_horizontal)
    # print(tiles_vertical)

    if tiles_horizontal:
        words.append(get_horizontal_word(board, tiles_added))
    else:
        for tile in tiles_added:
            words.append(get_horizontal_word(board, [tile]))

    if tiles_vertical:
        words.append(get_vertical_word(board, tiles_added))
    else:
        for tile in tiles_added:
            words.append(get_vertical_word(board, [tile]))

    # print(f'>>>{words}')
    # remove the single letter words
    words = [word for word in words if len(word) > 1]

    return words

def get_word_from_tiles(tiles):
    return ''.join([tile.letter for tile in tiles])

def test():

    board = [
        [ '',  '',  '',  '',  ''],
        [ '',  '', 't',  '',  ''],
        [ '', 'h', 'o', 'n',  ''],
        [ '',  '',  '',  '',  ''],
        [ '',  '',  '',  '',  ''],
    ]

    # to -> top
    # s-to-p
    # hon -> hon-k
    # hon -> p-hon-e
    # t -> t-o + o-n
    # ka-h + a-t

    words = get_words_for_new_tiles(board, [Tile('p', 2, 3)])
    # print(f'###{words}')
    assert(len(words) == 1)
    assert(len(words[0]) == 3)
    # print(words)
    assert(get_word_from_tiles(words[0]) == 'top')
    words = get_words_for_new_tiles(board, [Tile('s', 2, 0), Tile('p', 2, 3)])
    assert(len(words) == 1)
    assert(get_word_from_tiles(words[0]) == 'stop')
    # print(words)
    words = get_words_for_new_tiles(board, [Tile('k', 4, 2)])
    assert(len(words) == 1)
    assert(get_word_from_tiles(words[0]) == 'honk')
    words = get_words_for_new_tiles(board, [Tile('p', 0, 2), Tile('e', 4, 2)])
    assert(len(words) == 1)
    assert(get_word_from_tiles(words[0]) == 'phone')
    words = get_words_for_new_tiles(board, [Tile('o', 3, 1)])
    assert(len(words) == 2)
    assert(get_word_from_tiles(words[0]) == 'to')
    assert(get_word_from_tiles(words[1]) == 'on')
    words = get_words_for_new_tiles(board, [Tile('k', 1, 0), Tile('a', 1, 1)])
    # print(words)
    assert(len(words) == 2)
    assert(get_word_from_tiles(words[0]) == 'at')
    assert(get_word_from_tiles(words[1]) == 'kah')

if __name__ == "__main__":
    if sys.argv[1] == 'test':
        test()
