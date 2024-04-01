from itertools import combinations as cb
n = int(input())
health = list(map(int, input().split()))
smile = list(map(int, input().split()))

avail = [[i, j] for i, j in zip(health, smile)]
answer = 0

for i in range(1, 21):
    for j in cb(avail, i):
        cur = 100
        sm = 0
        for k in j:
            cur -= k[0]
            if cur > 0:
                sm += k[1]
                if sm > answer:
                    answer = sm
            else:
                break
print(answer)


'''
from sys import stdin

n = int(stdin.readline())
stamina_consum = [0] + list(map(int, stdin.readline().split()))
get_pleasure = [0] + list(map(int, stdin.readline().split()))

dp = [[0] * 101 for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, 101):
        if stamina_consum[i] <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j - stamina_consum[i]] + get_pleasure[i])
        else:
            dp[i][j] = dp[i-1][j]
    print(dp)
print(dp[n][99])
'''
