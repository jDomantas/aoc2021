from helpers import run


def hit(x0, x1, y0, y1, vx, vy):
    x = 0
    y = 0
    while x <= x1 and (y >= y0 or vy > 0):
        x += vx
        y += vy
        if x in range(x0, x1 + 1) and y in range(y0, y1 + 1):
            return True
        if vx > 0:
            vx -= 1
        vy -= 1
    return False


def solve(inp):
    _, _, xr, yr = inp.split()
    x0, x1 = xr[2:-1].split('..')
    x0 = int(x0)
    x1 = int(x1)
    y0, y1 = yr[2:].split('..')
    y0 = int(y0)
    y1 = int(y1)
    best_h = None
    if y0 >= 0 or y1 >= 0:
        raise Exception("unimplemented")
    cnt = 0
    for vx in range(0, x1 + 1):
        for vy in range(y0 - 1, -y0 + 1):
            if hit(x0, x1, y0, y1, vx, vy):
                h = 0 if vy <= 0 else vy * (vy + 1) // 2
                if best_h is None or best_h < h:
                    best_h = h
                cnt += 1
    print('part 1:', best_h)
    print('part 2:', cnt)


run(17, solve)
