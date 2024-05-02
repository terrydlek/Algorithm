import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ladder = {}
for _ in range(n):
    a, b = map(int, input().split())
    ladder[a] = b

snake = {}
for _ in range(m):
    a, b = map(int, input().split())
    snake[a] = b

dp = [101] * 101
dp[1] = 0
start = 1

for _ in range(2):
    for i in range(1, 101):
        for j in range(i + 1, i + 7):
            if j <= 100:
                cur = j
                if j in ladder:
                    cur = ladder[j]
                if j in snake:
                    cur = snake[j]
                dp[cur] = min(dp[i] + 1, dp[cur])

print(dp[-1])
