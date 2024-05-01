import sys
input = sys.stdin.readline

n = int(input())

'''
1 - 3 - 5 - 11 - 
21 - 43 - 85 - 171
'''

dp = [1, 1] + [0] * 999
for i in range(2, 1001):
    if i % 2 == 0:
        dp[i] = (dp[i - 1] * 2 + 1) % 10007
    else:
        dp[i] = (dp[i - 1] * 2 - 1) % 10007

print(dp[n])
