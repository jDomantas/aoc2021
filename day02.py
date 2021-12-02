from helpers import run


def parse(inp):
    steps = []
    for line in inp.splitlines():
        dir, dist = line.split(' ')
        dist = int(dist)
        if dir == 'down':
            steps.append((0, dist))
        elif dir == 'up':
            steps.append((0, -dist))
        elif dir == 'forward':
            steps.append((dist, 0))
        else:
            raise Exception('invalid input: ' + line)
    return steps


def solve(inp):
    steps = parse(inp)

    x = sum(dx for dx, _ in steps)
    depth = sum(dd for _, dd in steps)
    print('part 1:', x * depth)

    x = 0
    depth = 0
    aim = 0
    for dd, da in steps:
        aim += da
        x += dd
        depth += aim * dd
    print('part 2:', x * depth)


run(2, solve)
