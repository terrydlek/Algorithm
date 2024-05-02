import sys
import copy
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(input().strip()))

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

one = 0
q = deque()
nrgb = copy.deepcopy(graph)
for i in range(n):
    for j in range(n):
        if nrgb[i][j] != -1:
            q.append((i, j))
            crt = nrgb[i][j]
            while q:
                y, x = q.popleft()
                if not (0 <= y < n and 0 <= x < n and nrgb[y][x] != -1 and nrgb[y][x] == crt):
                    continue
                nrgb[y][x] = -1
                for k in range(4):
                    q.append((y + dy[k], x + dx[k]))
            one += 1
two = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] != -1:
            q.append((i, j))
            if graph[i][j] in ('R', 'G'):
                crt = ('R', 'G')
            else:
                crt = (graph[i][j])
            while q:
                y, x = q.popleft()
                if not (0 <= y < n and 0 <= x < n and graph[y][x] != -1 and graph[y][x] in crt):
                    continue
                graph[y][x] = -1
                for k in range(4):
                    q.append((y + dy[k], x + dx[k]))
            two += 1

print(one, two)
