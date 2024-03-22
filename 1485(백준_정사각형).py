import sys
from collections import defaultdict
t = int(input())

for _ in range(t):
    dot = []
    for _ in range(4):
        dot.append(list(map(int, sys.stdin.readline().split())))
    dic = defaultdict(int)
    for i in range(4):
        for j in range(4):
            if i != j:
                cal = ((dot[i][0] - dot[j][0])**2 + (dot[i][1] - dot[j][1])**2)**0.5
                dic[cal] += 1
    if len(dic) == 2:
        print(1)
    else:
        print(0)
