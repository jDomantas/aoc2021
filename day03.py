from helpers import run
from collections import Counter


def common(x):
    counts = Counter(x)
    return '1' if counts['1'] >= counts['0'] else '0'


def part1(values):
    bits = len(values[0])
    gamma = ""
    for i in range(bits):
        gamma += common(value[i] for value in values)
    gamma = int(gamma, 2)
    epsilon = 2 ** bits - 1 - gamma
    return gamma * epsilon


def find(values, selector):
    bits = len(values[0])
    for i in range(bits):
        bit = selector(v[i] for v in values)
        values = [v for v in values if v[i] == bit]
        if len(values) == 1:
            return values[0]
    raise Exception('{} values left'.format(len(values)))


def part2(values):
    oxygen = find(values, common)
    co2 = find(values, lambda x: str(1 - int(common(x))))
    return int(oxygen, 2) * int(co2, 2)


def solve(inp):
    values = inp.splitlines()
    print('part1:', part1(values))
    print('part2:', part2(values))
    

run(3, solve)
