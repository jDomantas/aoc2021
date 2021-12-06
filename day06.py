from helpers import run
from collections import Counter


def step(counts):
    result = [0] * 9
    result[8] += counts[0]
    result[6] += counts[0]
    for i in range(1, 9):
        result[i - 1] += counts[i]
    return result


def solve(inp):
    counts = [0] * 9
    for x in inp.split(','):
        counts[int(x)] += 1
    for _ in range(80):
        counts = step(counts)
    print('part 1:', sum(counts))
    for _ in range(256 - 80):
        counts = step(counts)
    print('part 2:', sum(counts))


run(6, solve)
