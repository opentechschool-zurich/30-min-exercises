from dataclasses import dataclass, field
from typing import List
from itertools import islice
# https://docs.python.org/3/library/itertools.html#itertools.batched
try:
    from itertools import batched # from python 3.12
except:
    def batched(iterable, n):
        # batched('ABCDEFG', 3) --> ABC DEF G
        if n < 1:
            raise ValueError('n must be at least one')
        it = iter(iterable)
        while batch := tuple(islice(it, n)):
            yield batch

data = """
Ic4 0000    0010    0000    0100
    1111    0010    0000    0100
    0000    0010    1111    0100
    0000    0010    0000    0100
Jb3 100     011     000     010 
    111     010     111     010 
    000     010     001     110 

Lo3 0000    000     000     000 
    0000    000     000     000 
    0000    000     000     000 

Oy4 0010    0100    0000    0000
    1110    0100    0000    0000
    0000    0110    0000    0000
    0000    0000    0000    0000
Sg3 011     010     000     100 
    110     011     011     110 
    000     001     110     010 

Tp3 010     010     000     010 
    111     011     111     110 
    000     010     010     010 

Zr3 110     001     000     010 
    011     011     110     110 
    000     010     011     100 

""".lstrip()

@dataclass
class Piece:
    name: str
    color: str
    bitmaps: List[bool] = field(default_factory=list)

rows = data.split('\n')
print(rows)
piece_data = []
for row in rows:
    piece_data.append(row)
    if len(piece_data) < 4:
        continue
    piece = Piece(piece_data[0][0], piece_data[0][1])
    bitmap_size = int(piece_data[0][2])
    for i, piece_row in enumerate([row[4:] for row in piece_data]):
        # print(piece_row)
        for piece_cell in batched(piece_row, 8):
            # print(piece_cell)
            piece.bitmaps.append(piece_cell[0:bitmap_size])
    print(piece)

    piece_data = []
