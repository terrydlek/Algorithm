import math
t = int(input())

tc = [list(map(int, input().split())) for _ in range(t)]
for j, i in enumerate(tc):
    a, b = i
    gcd = math.gcd(a, b)
    for k in range(a, b):
        gcd = math.gcd(gcd, k)
        if gcd == 1:
            break
    print(f'#{j + 1} {gcd}')
