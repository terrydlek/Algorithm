import sys
input = sys.stdin.readline

n = int(input())
stair = []
dp = [0] * (n + 1)

for _ in range(n):
    stair.append(int(input()))

if n == 1:
    print(stair[0])
elif n == 2:
    print(stair[0] + stair[1])
else:
    dp[1] = stair[0]
    dp[2] = stair[0] + stair[1]

    for i in range(3, n + 1):
        one = dp[i - 2] + stair[i - 1]
        two = dp[i - 3] + stair[i - 2] + stair[i - 1]
        dp[i] = max(one, two)
    print(dp[-1])
