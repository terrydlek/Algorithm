import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 0, 0, 1, 0, 0]
dy = [0, -1, 0, 0, 1, 0]
dz = [0, 0, -1, 0, 0, 1]

m, n, h = map(int, input().split())

tmt = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

q = deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if tmt[i][j][k] == 1:
                q.append((i, j, k))

while q:
    x, y, z = q.popleft()
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m and tmt[nx][ny][nz] == 0:
            tmt[nx][ny][nz] = tmt[x][y][z] + 1
            q.append((nx, ny, nz))

answer = -1e9
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tmt[i][j][k] == 0:
                answer = 1e9
            answer = max(answer, tmt[i][j][k])

if answer == 1e9:
    print(-1)
else:
    print(answer - 1)
