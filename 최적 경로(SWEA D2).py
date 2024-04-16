from itertools import permutations as pt

tc = int(input())
for rk in range(tc):
    n = int(input())
    idx = list(map(int, input().split()))
    company = (idx[0], idx[1])
    home = (idx[2], idx[3])
    away = [(idx[i], idx[i + 1]) for i in range(4, len(idx), 2)]
    answer = 1e9
    for i in pt(away, n):
        cnt = 0
        start = company
        for j in i:
            cnt += (abs(start[0] - j[0]) + abs(start[1] - j[1]))
            start = j
        cnt += (abs(start[0] - home[0]) + abs(start[1] - home[1]))
        if answer > cnt:
            answer = cnt
    print(f'#{rk + 1} {answer}')
