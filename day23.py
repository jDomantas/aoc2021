from helpers import run
import heapq


def kind_cost(p):
    if p == 'A': return 1
    if p == 'B': return 10
    if p == 'C': return 100
    if p == 'D': return 1000
    raise Exception(p)


COR_SLOTS = set([0, 1, 3, 5, 7, 9, 10])


def put(s, i, c):
    return s[:i] + c + s[i+1:]


def transitions(state):
    cor, a, b, c, d = state
    for idx, x, f, k in [(1, 2, a, 'A'), (2, 4, b, 'B'), (3, 6, c, 'C'), (4, 8, d, 'D')]:
        if all(i == k or i == '.' for i in f):
            # all correct, only insert
            slot = 0
            while slot + 1 < len(f) and f[slot + 1] == '.':
                slot += 1
            for cx in range(x, 11):
                if cor[cx] == k:
                    mc = (slot + 1 + abs(cx - x)) * kind_cost(k)
                    ncor = put(cor, cx, '.')
                    st = [ncor, a, b, c, d]
                    st[idx] = put(f, slot, k)
                    yield (mc, tuple(st))
                if cor[cx] != '.':
                    break
            for cx in range(x, -1, -1):
                if cor[cx] == k:
                    mc = (slot + 1 + abs(cx - x)) * kind_cost(k)
                    ncor = put(cor, cx, '.')
                    st = [ncor, a, b, c, d]
                    st[idx] = put(f, slot, k)
                    yield (mc, tuple(st))
                if cor[cx] != '.':
                    break
            pass
        else:
            # not correct, only remove
            slot = 0
            while f[slot] == '.':
                slot += 1
            for cx in range(x, 11):
                if cor[cx] != '.':
                    break
                if cx in COR_SLOTS:
                    mc = (slot + 1 + abs(cx - x)) * kind_cost(f[slot])
                    ncor = put(cor, cx, f[slot])
                    st = [ncor, a, b, c, d]
                    st[idx] = put(f, slot, '.')
                    yield (mc, tuple(st))
            for cx in range(x, -1, -1):
                if cor[cx] != '.':
                    break
                if cx in COR_SLOTS:
                    mc = (slot + 1 + abs(cx - x)) * kind_cost(f[slot])
                    ncor = put(cor, cx, f[slot])
                    st = [ncor, a, b, c, d]
                    st[idx] = put(f, slot, '.')
                    yield (mc, tuple(st))


def parse_state(inp):
    cor = '...........'
    a, b, c, d = '', '', '', ''
    for line in inp.splitlines():
        if line[3] == '#' or line[3] == '.':
            continue
        a += line[3]
        b += line[5]
        c += line[7]
        d += line[9]
    return cor, a, b, c, d


def target_state(inp):
    cor = '...........'
    a, b, c, d = '', '', '', ''
    for line in inp.splitlines():
        if line[3] == '#' or line[3] == '.':
            continue
        a += 'A'
        b += 'B'
        c += 'C'
        d += 'D'
    return cor, a, b, c, d


def path(state, target):
    queue = [(0, state)]
    cost = dict()
    while len(queue) > 0:
        c, s = heapq.heappop(queue)
        if s in cost:
            continue
        if s == target:
            return c
        cost[s] = c
        for cc, ss in transitions(s):
            if ss not in cost:
                heapq.heappush(queue, (c + cc, ss))
    raise Exception('no path')


def make_part2(inp):
    lines = inp.splitlines()
    return '\n'.join(lines[:3] + ['  #D#C#B#A#', '  #D#B#A#C#'] + lines[3:])


def solve(inp):
    state = parse_state(inp)
    target = target_state(inp)
    print('part 1:', path(state, target))
    inp = make_part2(inp)
    state = parse_state(inp)
    target = target_state(inp)
    print('part 2:', path(state, target))


run(23, solve)
