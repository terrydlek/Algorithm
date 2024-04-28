import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dp = [0] * (n + 1)
avail = list(map(int, input().split()))

for i, j in enumerate(avail):
    dp[i + 1] = dp[i] + j

for _ in range(m):
    start, end = map(int, input().split())
    print(dp[end] - dp[start - 1])
