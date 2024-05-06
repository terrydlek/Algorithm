import sys
from collections import deque

t = int(input())

for _ in range(t):
    check = [0] * 10001
    a, b = map(int, input().split())

    q = deque()
    q.append((a, ''))
    check[a] = 1

    while q:
        n, oper = q.popleft()

        if n == b:
            print(oper)
            break
        # D
        d = (n * 2) % 10000
        if not check[d]:
            check[d] = 1
            q.append((d, oper + 'D'))

        # S
        s = (n - 1) % 10000
        if not check[s]:
            check[s] = 1
            q.append((s, oper + 'S'))

        # L
        l = (n % 1000) * 10 + n // 1000
        if not check[l]:
            check[l] = 1
            q.append((l, oper + 'L'))

        # R
        r = (n % 10) * 1000 + n // 10
        if not check[r]:
            check[r] = 1
            q.append((r, oper + 'R'))
