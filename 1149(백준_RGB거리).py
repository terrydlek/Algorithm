import sys
input = sys.stdin.readline

n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]

for i in range(len(cost) - 1):
    cost[i + 1][0] += min(cost[i][1], cost[i][2])
    cost[i + 1][1] += min(cost[i][0], cost[i][2])
    cost[i + 1][2] += min(cost[i][0], cost[i][1])

print(min(cost[-1]))
