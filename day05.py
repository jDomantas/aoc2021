from helpers import run
from collections import Counter


def sign(num):
    if num < 0:
        return -1
    if num > 0:
        return 1
    return 0


def add_line(line, counts, diagonal):
    start, end = line.split(' -> ')
    sx, sy = start.split(',')
    ex, ey = end.split(',')
    sx = int(sx)
    sy = int(sy)
    ex = int(ex)
    ey = int(ey)
    dx = sign(ex - sx)
    dy = sign(ey - sy)
    if (dx != 0 and dy != 0) != diagonal:
        return
    steps = max(abs(sx - ex), abs(sy - ey)) + 1
    for i in range(steps):
        x = sx + dx * i
        y = sy + dy * i
        counts.update([(x, y)])


def solve(inp):
    c = Counter()
    for line in inp.splitlines():
        add_line(line, c, False)
    print('part 1:', sum(1 for k in c if c[k] >= 2))
    for line in inp.splitlines():
        add_line(line, c, True)
    print('part 2:', sum(1 for k in c if c[k] >= 2))


run(5, solve)
