from helpers import run
from dataclasses import dataclass


@dataclass
class Scanner:
    coord: tuple
    beacons: list


def parse(inp):
    scanners = []
    last = None
    for line in inp.splitlines():
        if line == '':
            continue
        elif line.startswith('---'):
            last = Scanner((0, 0, 0), [])
            scanners.append(last)
        else:
            x, y, z = line.split(',')
            last.beacons.append((int(x), int(y), int(z)))
    return scanners


def axes():
    yield (1, 0, 0)
    yield (0, 1, 0)
    yield (0, 0, 1)
    yield (-1, 0, 0)
    yield (0, -1, 0)
    yield (0, 0, -1)


def spaces():
    for x in axes():
        for y in axes():
            if x[0] * y[0] + x[1] * y[1] + x[2] * y[2] != 0:
                continue
            z0 = x[1] * y[2] - x[2] * y[1]
            z1 = x[2] * y[0] - x[0] * y[2]
            z2 = x[0] * y[1] - x[1] * y[0]
            yield x, y, (z0, z1, z2)


def orient(beacon, x, y, z):
    xx = beacon[0] * x[0] + beacon[1] * y[0] + beacon[2] * z[0]
    yy = beacon[0] * x[1] + beacon[1] * y[1] + beacon[2] * z[1]
    zz = beacon[0] * x[2] + beacon[1] * y[2] + beacon[2] * z[2]
    return (xx, yy, zz)


def oriented(scanner):
    for x, y, z in spaces():
        beacons = [orient(b, x, y, z) for b in scanner.beacons]
        yield Scanner((0, 0, 0), beacons)


def diffs(a):
    d = []
    a = sorted(a)
    for i in range(len(a)):
        x = a[i]
        for j in range(i + 1, len(a)):
            y = a[j]
            d.append((x[0] - y[0], x[1] - y[1], x[2] - y[2]))
    d.sort()
    return d


def same_count(a, b):
    i, j = 0, 0
    cnt = 0
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            cnt += 1
            i += 1
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1
    return cnt


def match_chance(a, b):
    diff_matches = same_count(diffs(a), diffs(b))
    return diff_matches >= 12 * 11 // 2


def match(a, b):
    if not match_chance(a.beacons, b.beacons):
        return None
    aa = set(a.beacons)
    if len(a.beacons) != len(aa): raise Exception('duplicated beacons')
    if len(b.beacons) != len(set(b.beacons)): raise Exception('duplicated beacons')
    for ax, ay, az in a.beacons:
        for bx, by, bz in b.beacons:
            matches = 0
            for x, y, z in b.beacons:
                x = x - bx + ax
                y = y - by + ay
                z = z - bz + az
                if (x, y, z) in aa:
                    matches += 1
            if matches >= 12:
                bb = [(ix - bx + ax, iy - by + ay, iz - bz + az) for ix, iy, iz in b.beacons]
                coord = (ax - bx, ay - by, az - bz)
                return Scanner(coord, bb)
    return None


def overlap(a, b):
    for bb in oriented(b):
        bbb = match(a, bb)
        if bbb is not None:
            return bbb
    return None


def find_match(ref, unmatched):
    for i in range(len(unmatched)):
        o = overlap(ref, unmatched[i])
        if o is not None:
            unmatched.pop(i)
            return o
    return None


def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])


def solve(inp):
    scanners = parse(inp)
    matched = [scanners[0]]
    scan_idx = 0
    unmatched = scanners[1:]
    while scan_idx < len(matched):
        x = find_match(matched[scan_idx], unmatched)
        if x is None:
            scan_idx += 1
        else:
            matched.append(x)
    print('part 1:', len(set(x for scanner in matched for x in scanner.beacons)))
    print('part 2:', max(dist(a.coord, b.coord) for a in matched for b in matched))


run(19, solve)
