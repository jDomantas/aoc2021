from helpers import run


class Die:
    def __init__(self):
        self.rolls = 0

    def roll(self):
        result = self.rolls % 100 + 1
        self.rolls += 1
        return result


def part1(p1, p2):
    s1, s2 = 0, 0
    die = Die()
    while True:
        p1 += die.roll() + die.roll() + die.roll()
        p1 %= 10
        s1 += p1 + 1
        if s1 >= 1000:
            break
        p2 += die.roll() + die.roll() + die.roll()
        p2 %= 10
        s2 += p2 + 1
        if s2 >= 1000:
            break
    return min(s1, s2) * die.rolls


def part2(p1, p2):
    cache = dict()
    def go(p1, p2, s1, s2):
        nonlocal cache
        key = (p1, p2, s1, s2)
        if key in cache:
            return cache[key]
        if s1 >= 21:
            cache[key] = (1, 0)
            return (1, 0)
        if s2 >= 21:
            cache[key] = (0, 1)
            return (0, 1)

        tot1 = 0
        tot2 = 0
        for i in range(1, 4):
            for j in range(1, 4):
                for k in range(1, 4):
                    tot = i + j + k
                    p1n = (p1 + tot) % 10
                    s1n = s1 + p1n + 1
                    w2, w1 = go(p2, p1n, s2, s1n)
                    tot1 += w1
                    tot2 += w2
        cache[key] = (tot1, tot2)
        return (tot1, tot2)
    return max(go(p1, p2, 0, 0))


def solve(inp):
    l1, l2 = inp.splitlines()
    p1 = int(l1[28:]) - 1
    p2 = int(l2[28:]) - 1
    print('part 1:', part1(p1, p2))
    print('part 2:', part2(p1, p2))


run(21, solve)
