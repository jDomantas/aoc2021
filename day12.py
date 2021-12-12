from helpers import run


def is_big(cave):
    return cave[0].isupper()


def is_small(cave):
    return cave[0].islower()


def solve(inp):
    edges = dict()
    small = set()
    paths = dict()
    for line in inp.splitlines():
        start, end = line.split('-')
        if is_big(start) and is_big(end):
            raise Exception('cannot solve')
        if start not in edges: edges[start] = []
        if end not in edges: edges[end] = []
        edges[start].append(end)
        edges[end].append(start)
        if is_small(start):
            small.add(start)
        if is_small(end):
            small.add(end)
    for a in small:
        paths[a] = dict()
        for b in small:
            if b != 'start':
                cnt = 0
                if b in edges[a]:
                    cnt += 1
                for c in edges[a]:
                    if is_big(c) and c in edges[b]:
                        cnt += 1
                paths[a][b] = cnt
    def go(at, visited):
        if at == 'end':
            return 1
        if at in visited:
            return 0
        visited.add(at)
        total = 0
        for ng, cnt in paths[at].items():
            if cnt > 0:
                total += cnt * go(ng, visited)
        visited.remove(at)
        return total
    def go2(at, visited):
        if at == 'end':
            return 1
        total = 0
        if at in visited:
            for ng, cnt in paths[at].items():
                if cnt > 0:
                    total += cnt * go(ng, visited)
        else:
            visited.add(at)
            for ng, cnt in paths[at].items():
                if cnt > 0:
                    total += cnt * go2(ng, visited)
            visited.remove(at)
        return total

    print('part 1:', go('start', set()))
    print('part 2:', go2('start', set()))


run(12, solve)
