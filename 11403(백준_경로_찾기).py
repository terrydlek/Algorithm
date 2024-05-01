import sys
from collections import deque
input = sys.stdin.readline


n = int(input())
graph = []
for i in range(n):
    route = list(map(int, input().split()))
    graph.append(route)

avail = [[0] * n for _ in range(n)]

for i in range(n):
    q = deque([i])
    visited = [0] * n
    while q:
        cur = q.popleft()
        if visited[cur] == 1:
            continue
        visited[cur] = 1
        for j in range(n):
            if graph[cur][j] == 1:
                avail[i][j] = 1
                q.append(j)

for i in avail:
    for j in i:
        print(j, end=' ')
    print()
