from helpers import run


def increases(depths):
    count = 0
    for i in range(1, len(depths)):
        if depths[i - 1] < depths[i]:
            count += 1
    return count


def solve(inp):
    depths = [int(line) for line in inp.splitlines()]
    print('part 1:', increases(depths))
    windows = [sum(depths[i:i+3]) for i in range(0, len(depths) - 2)]
    print('part 2:', increases(windows))


run(1, solve)
