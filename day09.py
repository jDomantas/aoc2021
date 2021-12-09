from helpers import run


def neighbours(r, c):
    yield (r - 1, c)
    yield (r + 1, c)
    yield (r, c - 1)
    yield (r, c + 1)


def solve(inp):
    rows = [
        [int(x) for x in line]
        for line in inp.splitlines()
    ]
    width = len(rows[0])
    height = len(rows)

    def get(r, c):
        if r not in range(height) or c not in range(width):
            return 999
        return rows[r][c]

    marked = set()
    def basin(r, c):
        if r not in range(height) or c not in range(width):
            return 0
        if (r, c) in marked:
            return 0
        marked.add((r, c))
        v = get(r, c)
        if v == 9:
            return 0
        size = 1
        for nr, nc in neighbours(r, c):
            if get(nr, nc) > v:
                size += basin(nr, nc)
        return size

    part1 = 0
    sizes = []
    for r in range(height):
        for c in range(width):
            v = get(r, c)
            if all(v < get(nr, nc) for nr, nc in neighbours(r, c)):
                part1 += v + 1
                sizes.append(basin(r, c))
    print('part 1:', part1)
    sizes.sort()
    print('part 2:', sizes[-1] * sizes[-2] * sizes[-3])


run(9, solve)
