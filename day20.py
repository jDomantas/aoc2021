from helpers import run
from dataclasses import dataclass


@dataclass
class Grid:
    cells: dict
    outside: bool
    def get(self, x, y):
        if (x, y) in self.cells:
            return self.cells[x, y]
        return self.outside


def ng(x, y):
    yield x - 1, y - 1
    yield x, y - 1
    yield x + 1, y - 1
    yield x - 1, y
    yield x, y
    yield x + 1, y
    yield x - 1, y + 1
    yield x, y + 1
    yield x + 1, y + 1


def step(grid, rule):
    min_x = min(x for x, _ in grid.cells)
    max_x = max(x for x, _ in grid.cells)
    min_y = min(y for _, y in grid.cells)
    max_y = max(y for _, y in grid.cells)
    new_mark = dict()
    for x in range(min_x - 1, max_x + 2):
        for y in range(min_y - 1, max_y + 2):
            tot = 0
            for xx, yy in ng(x, y):
                tot *= 2
                if grid.get(xx, yy):
                    tot += 1
            new_mark[x, y] = rule[tot]
    outside = rule[-1] if grid.outside else rule[0]
    return Grid(new_mark, outside)


def show(grid):
    min_x = min(x for x, _ in grid.cells)
    max_x = max(x for x, _ in grid.cells)
    min_y = min(y for _, y in grid.cells)
    max_y = max(y for _, y in grid.cells)
    for y in range(min_y - 3, max_y + 3):
        for x in range(min_x - 3, max_x + 3):
            if grid.get(x, y):
                print('#', end = '')
            else:
                print('.', end = '')
        print()


def solve(inp):
    lines = inp.splitlines()
    rule = [x == '#' for x in lines[0]]
    cells = dict()
    for (y, row) in enumerate(lines[2:]):
        for (x, c) in enumerate(row):
            cells[x, y] = (c == '#')
    grid = Grid(cells, False)
    for _ in range(2):
        grid = step(grid, rule)
    if grid.outside:
        print('part 1: infinity')
    else:
        print('part 1:', sum(grid.cells.values()))
    for _ in range(50 - 2):
        grid = step(grid, rule)
    if grid.outside:
        print('part 2: infinity')
    else:
        print('part 2:', sum(grid.cells.values()))


run(20, solve)
