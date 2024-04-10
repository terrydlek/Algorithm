import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
grph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    grph[a].append(b)
    grph[b].append(a)

def bfs(grph, start):
    visited = [start]
    num = [0] * (n + 1)
    q = deque()
    q.append(start)
    while q:
        cur = q.popleft()
        for i in grph[cur]:
            if i not in visited:
                q.append(i)
                visited.append(i)
                num[i] = num[cur] + 1
    return sum(num)

answer, crt = 1e9, 1e9

for i in range(1, n + 1):
    cnt = bfs(grph, i)
    if cnt < crt:
        crt = cnt
        answer = i
print(answer)
