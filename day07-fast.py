from helpers import run


def total(x):
    return x * (x + 1) // 2


def solve(inp):
    nums = sorted(int(x) for x in inp.split(','))
    median = nums[len(nums) // 2]
    print('part 1:', sum(abs(x - median) for x in nums))
    d1, s1 = 0, 0
    d2 = sum(x - nums[0] for x in nums)
    s2 = sum(total(x - nums[0]) for x in nums)
    idx = 0
    best = s2
    for i in range(nums[0] + 1, nums[-1] + 1):
        while idx < len(nums) and nums[idx] < i:
            idx += 1
            d1 += 1
        s1 += d1
        d1 += idx
        s2 -= d2
        d2 -= len(nums) - idx
        if s1 + s2 < best:
            best = s1 + s2
    print('part 2:', best)


run(7, solve)
