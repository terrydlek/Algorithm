import sys
input = sys.stdin.readline

n = int(input())
avail = []
for _ in range(n):
    wh = list(map(int, input().split()))
    avail.append(wh)

answer = []
for i in range(n):
    rank = 0
    for j in range(n):
        if avail[i][0] < avail[j][0] and avail[i][1] < avail[j][1]:
            rank += 1
    answer.append(rank + 1)
for i in answer:
    print(i, end=' ')

