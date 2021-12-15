from helpers import run


def solve(inp):
    points = set()
    part1 = None
    for line in inp.splitlines():
        if line.startswith('fold along'):
            coord = int(line[13:])
            if line[11] == 'x':
                points = {(x if x <= coord else 2 * coord - x, y) for x, y in points}
            else:
                points = {(x, y if y <= coord else 2 * coord - y) for x, y in points}
            if part1 is None:
                part1 = len(points)
        elif ',' in line:
            x, y = line.split(',')
            points.add((int(x), int(y)))
    print('part 1:', part1)
    x0 = min(x for x, _ in points)
    y0 = min(y for _, y in points)
    x1 = max(x for x, _ in points)
    y1 = max(y for _, y in points)
    print('part 2:')
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            if (x, y) in points:
                print('#', end = '')
            else:
                print('.', end = '')
        print()


run(13, solve)
