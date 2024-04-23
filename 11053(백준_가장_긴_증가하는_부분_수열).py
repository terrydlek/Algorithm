import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n + 1)
avail = [0] + list(map(int, input().split()))
dp[1] = 1
for i in range(2, n + 1):
    dp[i] = 1
    for j in range(1, i):
        if avail[i] > avail[j]:
            dp[i] = max(dp[i], 1 + dp[j])
print(max(dp))
