import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    h, w, n = map(int, input().split())
    cnt = 0
    fl, ho = '', ''
    for i in range(1, w + 1):
        for j in range(1, h + 1):
            cnt += 1
            if cnt == n:
                fl, ho = str(j), str(i)
                break
    if len(ho) < 2:
        ho = '0' + ho
    print(fl + ho)
    