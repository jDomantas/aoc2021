from helpers import run
from collections import Counter


def counts(pair, rules, steps, cache):
    if steps == 0:
        return Counter()
    if (pair, steps) in cache:
        return cache[pair, steps]
    inner = rules[pair]
    left = counts(pair[0] + inner, rules, steps - 1, cache)
    right = counts(inner + pair[1], rules, steps - 1, cache)
    result = Counter([inner]) + left + right
    cache[pair, steps] = result
    return result


def score(counts):
    return max(counts.values()) - min(counts.values())


def solve(inp):
    lines = inp.splitlines()
    init = lines[0]
    rules = dict()
    for rule in lines[2:]:
        a, b = rule.split(' -> ')
        rules[a] = b
    cache = dict()
    part1 = Counter(init)
    part2 = Counter(init)
    for i in range(1, len(init)):
        pair = init[i - 1 : i + 1]
        part1 += counts(pair, rules, 10, cache)
        part2 += counts(pair, rules, 40, cache)
    print('part 1:', score(part1))
    print('part 2:', score(part2))


run(14, solve)