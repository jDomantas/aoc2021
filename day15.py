from helpers import run
import heapq


def path(tiles):
    w = len(tiles[0])
    h = len(tiles)
    def ng(x, y):
        if x > 0: yield x - 1, y
        if y > 0: yield x, y - 1
        if x < w - 1: yield x + 1, y
        if y < h - 1: yield x, y + 1
    cost = dict()
    queue = [(0, 0, 0)]
    steps = 0
    while len(queue) > 0:
        c, x, y = heapq.heappop(queue)
        if (x, y) in cost:
            continue
        cost[x, y] = c
        for xx, yy in ng(x, y):
            if (xx, yy) not in cost:
                heapq.heappush(queue, (cost[x, y] + tiles[yy][xx], xx, yy))
        steps += 1
    return cost[w - 1, h - 1]


def solve(inp):
    tiles = [
        [int(x) for x in row]
        for row in inp.splitlines()
    ]
    print('part 1:', path(tiles))
    w = len(tiles[0])
    h = len(tiles)
    tiles2 = [
        [(tiles[y % h][x % w] + (x // w) + (y // h) - 1) % 9 + 1 for x in range(w * 5)]
        for y in range(h * 5)
    ]
    print('part 2:', path(tiles2))


run(15, solve)
