from helpers import run
from itertools import permutations
from collections import Counter


symbols = {
    'abcefg': 0,
    'cf': 1,
    'acdeg': 2,
    'acdfg': 3,
    'bcdf': 4,
    'abdfg': 5,
    'abdefg': 6,
    'acf': 7,
    'abcdefg': 8,
    'abcdfg': 9,
}


def unmangle(symbols):
    symbols = [''.join(sorted(sym)) for sym in symbols]
    mapping = dict()
    unmapped = []
    for key in symbols:
        if len(key) == 2:
            mapping[key] = 1
        elif len(key) == 3:
            mapping[key] = 7
        elif len(key) == 4:
            mapping[key] = 4
        elif len(key) == 7:
            mapping[key] = 8
        else:
            unmapped.append(key)
    counts = Counter(c for x in unmapped for c in x)
    e = next(ch for ch in counts if counts[ch] == 3)
    for key in symbols:
        if len(key) == 5 and e in key:
            mapping[key] = 2
        elif len(key) == 6 and e not in key:
            mapping[key] = 9
    unmapped = []
    for sym in symbols:
        if sym not in mapping:
            unmapped.append(sym)
    for a in unmapped:
        if len(a) != 5:
            continue
        for b in unmapped:
            if len(b) != 6:
                continue
            if set(a).issubset(set(b)):
                mapping[a] = 5
                mapping[b] = 6
    for sym in unmapped:
        if len(sym) == 5 and sym not in mapping:
            mapping[sym] = 3
        elif len(sym) == 6 and sym not in mapping:
            mapping[sym] = 0
    return mapping


def solve(inp):
    part1 = 0
    part2 = 0
    for line in inp.splitlines():
        check, test = line.split(' | ')
        mapping = unmangle(check.split())
        value = 0
        for sym in test.split():
            sym = ''.join(sorted(sym))
            if mapping[sym] in [1, 4, 7, 8]:
                part1 += 1
            value = 10 * value + mapping[sym]
        part2 += value
    print('part 1:', part1)
    print('part 2:', part2)


run(8, solve)
