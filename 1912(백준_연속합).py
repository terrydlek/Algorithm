import sys
input = sys.stdin.readline

n = int(input())
avail = [0] + list(map(int, input().split()))

dp = [0] * (n + 1)

for i in range(1, n + 1):
    one = dp[i - 1] + avail[i]
    two = avail[i]
    dp[i] = max(one, two)
print(max(dp[1:]))
