t = int(input())

for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    # print(x1, y1, r1, x2, y2, r2)
    if (x1, y1) == (x2, y2):
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        d = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
        if d == r1 + r2 or d == abs(r1 - r2):
            print(1)
        elif abs(r1 - r2) < d < r1 + r2:
            print(2)
        else:
            print(0)
