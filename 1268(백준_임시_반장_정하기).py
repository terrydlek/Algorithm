import sys

n = int(input())

std = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

past = [[] for _ in range(n)]

for i in range(5):
    for j in range(n):
        for k in range(j + 1, n):
            if std[j][i] == std[k][i]:
            # if std[j][i] == std[k][i] and k not in past[j]:
                past[j].append(k)
                past[k].append(j)

# print(past)

answer = 0
mx = -1
for i, j in enumerate(past):
    if len(set(j)) > mx:
        mx = len(set(j))
        answer = i + 1

print(answer)
# st = sorted(past, key=lambda x: len(x), reverse=True)
#
# mx = len(st[0])
#
# print(past.index(st[0]) + 1)
