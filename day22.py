from helpers import run


def parse_range(c):
    _, c = c.split('=')
    l, h = c.split('..')
    return int(l), int(h) + 1


def parse_query(q):
    state, coords = q.split()
    state = state == 'on'
    x, y, z = coords.split(',')
    x0, x1 = parse_range(x)
    y0, y1 = parse_range(y)
    z0, z1 = parse_range(z)
    return state, x0, x1, y0, y1, z0, z1


def compress(coords):
    coords = list(coords)
    coords.sort()
    mapping = dict()
    size = []
    for (i, c) in enumerate(coords):
        mapping[c] = i
        if i + 1 < len(coords):
            size.append(coords[i + 1] - coords[i])
    return mapping, size


def calc(queries):
    xm, xs = compress(x for _, x0, x1, _, _, _, _ in queries for x in [x0, x1])
    ym, ys = compress(y for _, _, _, y0, y1, _, _ in queries for y in [y0, y1])
    zm, zs = compress(z for _, _, _, _, _, z0, z1 in queries for z in [z0, z1])
    print('compressed: {} x {} x {}'.format(len(xs), len(ys), len(zs)))
    states = [
        [
            0
            for _ in ys
        ]
        for _ in zs
    ]
    for i, (state, x0, x1, y0, y1, z0, z1) in enumerate(queries):
        x0 = xm[x0]
        x1 = xm[x1]
        y0 = ym[y0]
        y1 = ym[y1]
        z0 = zm[z0]
        z1 = zm[z1]
        for x in range(x0, x1):
            for y in range(y0, y1):
                if state:
                    bits = ((1 << (z1 - z0)) - 1) << z0
                    states[x][y] |= bits
                else:
                    bits = (((1 << (z1 - z0)) - 1) << z0) & states[x][y]
                    states[x][y] ^= bits
    total = 0
    for (x, sx) in enumerate(xs):
        for (y, sy) in enumerate(ys):
            state = states[x][y]
            tt = 0
            for (z, sz) in enumerate(zs):
                if state & (1 << z):
                    tt += sz
            total += sx * sy * tt
    return total


def part1_queries(queries):
    for state, x0, x1, y0, y1, z0, z1 in queries:
        if x0 > 50 or x1 < -50:
            continue
        if y0 > 50 or y1 < -50:
            continue
        if z0 > 50 or z1 < -50:
            continue
        x0 = max(x0, -50)
        x1 = min(x1, 51)
        y0 = max(y0, -50)
        y1 = min(y1, 51)
        z0 = max(z0, -50)
        z1 = min(z1, 51)
        yield state, x0, x1, y0, y1, z0, z1


def solve(inp):
    queries = [parse_query(q) for q in inp.splitlines()]
    part1 = list(part1_queries(queries))
    print('part 1:', calc(part1))
    print('part 2:', calc(queries))


run(22, solve)
