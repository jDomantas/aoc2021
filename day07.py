from helpers import run

def solve(i):
    x=sorted([int(p)for p in i.split(',')])
    m=x[len(x)//2]
    print('part 1:',sum(abs(a-m)for a in x))
    s=lambda t:t*(t+1)//2
    print('part 2:',min(sum(s(abs(a-b))for a in x)for b in range(x[0],x[-1]+1)))


run(7, solve)
