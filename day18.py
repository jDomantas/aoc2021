from helpers import run
from functools import reduce


def parse(line):
    return [
        (x if x in '[]' else int(x))
        for x in (line
            .replace('[', ' [ ')
            .replace(']', ' ] ')
            .replace(',', ' ')
            .split())
    ]


def reduce_explode(num):
    idx = 0
    depth = 0
    while idx < len(num):
        if num[idx] == '[' and depth == 4:
            for i in range(idx + 3, len(num)):
                if type(num[i]) is int:
                    num[i] += num[idx + 2]
                    break
            for i in range(idx, -1, -1):
                if type(num[i]) is int:
                    num[i] += num[idx + 1]
                    break
            return num[:idx] + [0] + num[idx+4:]
        elif num[idx] == '[':
            depth += 1
        elif num[idx] == ']':
            depth -= 1
        idx += 1
    return None


def reduce_split(num):
    idx = 0
    while idx < len(num):
        if type(num[idx]) is int and num[idx] >= 10:
            left = num[idx] // 2
            right = num[idx] - left
            return num[:idx] + ['[', left, right, ']'] + num[idx+1:]
        idx += 1
    return None


def reduce_all(num):
    while True:
        next_num = reduce_explode(num)
        if next_num is None:
            next_num = reduce_split(num)
        if next_num is not None:
            num = next_num
        else:
            return num


class Traverse:
    def __init__(self, num):
        self.num = num
        self.idx = 0

    def enter_pair(self):
        if self.num[self.idx] == '[':
            self.idx += 1
            return True
        else:
            return False
    
    def eat_num(self):
        if type(self.num[self.idx]) is not int:
            raise Exception('not at num')
        self.idx += 1
        return self.num[self.idx - 1]
    
    def exit_pair(self):
        if self.num[self.idx] != ']':
            raise Exception('not at pair end')
        self.idx += 1


def magnitude(num):
    def go(t):
        if t.enter_pair():
            l = go(t)
            r = go(t)
            t.exit_pair()
            return 3 * l + 2 * r
        else:
            return t.eat_num()
    return go(Traverse(num))


def add(a, b):
    return reduce_all(['['] + a + b + [']'])


def solve(inp):
    fish = []
    for line in inp.splitlines():
        fish.append(parse(line))
    print('part 1:', magnitude(reduce(add, fish)))
    best = -1
    for i in range(len(fish)):
        for j in range(len(fish)):
            if i != j:
                x = magnitude(add(fish[i], fish[j]))
                if x > best:
                    best = x
    print('part 2:', best)


run(18, solve)
