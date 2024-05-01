import sys
input = sys.stdin.readline

n = int(input())
dp = [0, 1] + [0] * (n - 1)
for i in range(2, n + 1):
    mn = 4
    j = 1
    while (j ** 2) <= i:
        mn = min(mn, dp[i - j**2] + 1)
        j += 1
    dp[i] = mn
print(dp[n])
