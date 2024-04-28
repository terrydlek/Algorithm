import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (n + 1)
answer = 0
for i in range(n + 1):
    for j in graph[i]:
        if not visited[i]:
            answer += 1
            q = deque()
            q.append(i)
            while q:
                a = q.popleft()
                if visited[a]:
                    continue
                visited[a] = 1
                for k in graph[a]:
                    q.append(k)
for i in visited[1:]:
    if not i:
        answer += 1

print(answer)
