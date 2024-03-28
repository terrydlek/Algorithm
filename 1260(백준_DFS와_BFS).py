from collections import deque
n, m, v = map(int, input().split())
rd = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    rd[a].append(b)
    rd[b].append(a)

for i in range(len(rd)):
    rd[i].sort()

visited1 = [False] * (n + 1)
arr1 = []
def dfs(start):
    visited1[start] = True
    arr1.append(start)
    for i in rd[start]:
        if not visited1[i]:
            dfs(i)


dfs(v)
for i, j in enumerate(arr1):
    if i != len(arr1) - 1:
        print(j, end=' ')
    else:
        print(j)

visited2 = [False] * (n + 1)
arr2 = []
def bfs(start):
    q = deque()
    q.append(start)
    visited2[start] = True
    while q:
        node = q.popleft()
        arr2.append(node)
        visited2[node] = True
        for nbr in rd[node]:
            if not visited2[nbr]:
                q.append(nbr)
                visited2[nbr] = True


bfs(v)
for i, j in enumerate(arr2):
    if i != len(arr2) - 1:
        print(j, end=' ')
    else:
        print(j)
