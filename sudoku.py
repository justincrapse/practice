import math
from collections import OrderedDict

# http://www.websudoku.com/?level=1&set_id=9584958293
puzzle = [[0, 5, 0, 0, 0, 4, 0, 3, 9],
          [7, 4, 0, 6, 0, 0, 0, 0, 0],
          [0, 0, 3, 0, 0, 0, 0, 0, 7],
          [3, 0, 5, 7, 4, 0, 8, 9, 0],
          [0, 9, 0, 3, 2, 1, 0, 5, 0],
          [0, 7, 6, 0, 8, 9, 3, 0, 4],
          [9, 0, 0, 0, 0, 0, 4, 0, 0],
          [0, 0, 0, 0, 0, 3, 0, 6, 8],
          [4, 3, 0, 2, 0, 0, 0, 1, 0]]


def get_possible_values(entry, puzzle):
    row_values = puzzle[entry['x']]
    col_values = list(zip(*puzzle))[entry['y']]
    row_sec = entry['x'] // m_sec_size
    col_sec = entry['y'] // m_sec_size
    row_start = row_sec * m_sec_size
    col_start = col_sec * m_sec_size
    sec_values = [puzzle[x][y] for x in range(row_start, row_start + 3)
                  for y in range(col_start, col_start + 3)]
    return set(range(1, 10)) - (set(sec_values) | set(row_values) | set(col_values))


def solve_sudoku(puzzle):
    global m_size
    m_size = len(puzzle)
    global m_sec_size
    m_sec_size = int(math.sqrt(m_size))
    global m_slice
    m_slice = slice(0, m_size - m_sec_size + 1, m_sec_size)

    entries = {}
    entry = [0, 0]
    while entry != [m_size - 1, m_size]:
        x = entry[0]
        y = entry[1]

        if entry in [i.key for i in entries]:
            if entries[entry]:
                puzzle[x][y] = entries[entry].pop()
            else:
                pass


        if puzzle[x][y] == 0:
            values = get_possible_values([x, y], puzzle)
            entries[entry] = values

            if values:
                pass
            else:
                entry = entries[entry]
                continue

        if y < 9:
            entry[1] = y + 1
        else:
            entry[0] = x + 1
            entry[1] = 0


    return puzzle

results = solve_sudoku(puzzle)
for i in results:
    print(i)