t = int(input())

for _ in range(t):
    cnt = [[1, 0], [0, 1]]
    n = int(input())
    if n == 0 or n == 1:
        print(f'{cnt[n][0]} {cnt[n][1]}')
    else:
        for _ in range(n - 1):
            cnt[0], cnt[1] = cnt[1], [cnt[0][0] + cnt[1][0], cnt[0][1] + cnt[1][1]]
        print(f'{cnt[1][0]} {cnt[1][1]}')
