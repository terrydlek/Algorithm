import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    dp = [[0] * (n) for _ in range(2)]
    sticker = [list(map(int, input().split())) for _ in range(2)]
    answer = 0
    if n == 1:
        answer = max(sticker[0][0], sticker[1][0])
    elif n == 2:
        answer = max(sticker[0][0] + sticker[1][1], sticker[1][0] + sticker[0][1])
    else:
        dp[0][0], dp[1][0] = sticker[0][0], sticker[1][0]
        dp[0][1], dp[1][1] = sticker[1][0] + sticker[0][1], sticker[1][1] + sticker[0][0]
        for i in range(2, n):
            dp[0][i] = sticker[0][i] + max(dp[1][i - 1], dp[1][i - 2])
            dp[1][i] = sticker[1][i] + max(dp[0][i - 1], dp[0][i - 2])
        answer = max(max(dp[0]), max(dp[1]))
    print(answer)
