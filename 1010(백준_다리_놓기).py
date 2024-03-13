import math

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    if 0 in [n, m]:
        print(0)
    else:
        print(math.factorial(m) // math.factorial(n) // math.factorial(m - n))
