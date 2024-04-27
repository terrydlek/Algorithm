import sys
input = sys.stdin.readline

t = int(input())

member = [[i for i in range(1, 15)]] + [[] * (15) for _ in range(14)]

for i in range(1, 15):
    for j in range(1, 15):
        member[i].append(sum(member[i - 1][:j]))

for _ in range(t):
    k = int(input())
    n = int(input())
    print(member[k][n - 1])
