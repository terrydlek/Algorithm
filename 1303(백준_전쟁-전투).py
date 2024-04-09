import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
gph = [list(input().strip()) for _ in range(m)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

count = {'W': 0, 'B': 0}


def dfs(y, x):
    q = deque()
    q.append((y, x))
    cur = gph[y][x]
    cnt = 0
    while q:
        cury, curx = q.popleft()
        if not (0 <= cury < m and 0 <= curx < n and gph[cury][curx] == cur):
            continue
        gph[cury][curx] = '0'
        cnt += 1
        for i in range(4):
            q.append((cury + dy[i], curx + dx[i]))
    return (cur, cnt)


for i in range(m):
    for j in range(n):
        if gph[i][j] != '0':
            idx, cnt = dfs(i, j)
            count[idx] += cnt*cnt

print(count['W'], count['B'])
