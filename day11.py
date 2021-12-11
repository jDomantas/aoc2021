from helpers import run


def neighbours(r, c):
    for rr in range(r - 1, r + 2):
        for cc in range(c - 1, c + 2):
            if rr != r or cc != c:
                yield rr, cc


def solve(inp):
    table = [
        [int(x) for x in row]
        for row in inp.splitlines()
    ]
    w = len(table[0])
    h = len(table)
    flashes = 0
    def trigger(r, c):
        nonlocal flashes
        if r not in range(h) or c not in range(w):
            return
        table[r][c] += 1
        if table[r][c] == 10:
            flashes += 1
            for rr, cc in neighbours(r, c):
                trigger(rr, cc)
    part1 = None
    part2 = None
    step = 0
    while part1 is None or part2 is None:
        before = flashes
        for r in range(h):
            for c in range(w):
                trigger(r, c)
        for r in range(h):
            for c in range(w):
                if table[r][c] >= 10:
                    table[r][c] = 0
        step += 1
        if step == 100:
            part1 = flashes
        if flashes - before == w * h:
            part2 = step
    print('part 1:', part1)
    print('part 2:', part2)


run(11, solve)
