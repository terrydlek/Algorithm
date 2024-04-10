import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

grph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    grph[b].append(a)
def bfs(grph, start):
    visited = [0] * (n + 1)
    visited[start] = 1
    q = deque()
    q.append(start)
    while q:
        a = q.popleft()
        for i in grph[a]:
            if visited[i] == 0:
                visited[i] = 1
                q.append(i)
    return sum(visited)


ans = [0] * (n + 1)
for i in range(1, n + 1):
    ans[i] = bfs(grph, i)
mx = max(ans)
for i, j in enumerate(ans):
    if j == mx:
        print(i, end=' ')
