from helpers import run


def err(line):
    stack = []
    for c in line:
        if c in '({[<':
            stack.append(')}]>'['({[<'.find(c)])
        elif len(stack) > 0 and stack[-1] == c:
            stack.pop()
        else:
            return c
    return None


def complete(line):
    stack = []
    for c in line:
        if c in '({[<':
            stack.append(')}]>'['({[<'.find(c)])
        elif len(stack) > 0 and stack[-1] == c:
            stack.pop()
        else:
            return None
    if len(stack) == 0:
        return None
    score = 0
    for c in stack[::-1]:
        score *= 5
        if c == ')': score += 1
        if c == ']': score += 2
        if c == '}': score += 3
        if c == '>': score += 4
    return score


def solve(inp):
    part1 = 0
    scores = []
    for line in inp.splitlines():
        e = err(line)
        if e == '>': part1 += 25137
        if e == ']': part1 += 57
        if e == '}': part1 += 1197
        if e == ')': part1 += 3
        score = complete(line)
        if score is not None:
            scores.append(score)
    scores.sort()
    print('part 1:', part1)
    print('part 2:', scores[len(scores) // 2])


run(10, solve)
