import sys
from itertools import combinations as cb
input = sys.stdin.readline

n = int(input())
grph = [input().split() for _ in range(n)]

answer = 1e9
avail = [i for i in range(1, n + 1)]

for i in cb(avail, n // 2):
    sc1, sc2 = 0, 0
    start = list(set(i))
    link = list(set(avail) - set(i))
    for j in range(n // 2):
        for k in range(j + 1, n // 2):
            sc1 += int(grph[start[j] - 1][start[k] - 1])
            sc1 += int(grph[start[k] - 1][start[j] - 1])
            sc2 += int(grph[link[j] - 1][link[k] - 1])
            sc2 += int(grph[link[k] - 1][link[j] - 1])
    if abs(sc1 - sc2) < answer:
        answer = abs(sc1 - sc2)
print(answer)
