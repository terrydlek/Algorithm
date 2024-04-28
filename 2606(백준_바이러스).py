import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
con = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(con):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque()
q.append(1)
visited = []
while q:
    cur = q.popleft()
    for i in graph[cur]:
        if i in visited:
            continue
        visited.append(i)
        q.append(i)
if not visited:
    print(0)
else:
    print(len(visited) - 1)
