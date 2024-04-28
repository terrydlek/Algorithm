import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
starty, startx = 0, 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            starty, startx = i, j
            break

answer = [[-1] * m for _ in range(n)]
answer[starty][startx] = 0
q = deque()

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

for i in range(4):
    q.append((starty + dy[i], startx + dx[i]))

while q:
    y, x = q.popleft()
    if not (0 <= y < n and 0 <= x < m and answer[y][x] == -1 and graph[y][x] != 0):
        continue
    cnt = 1e9
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        q.append((ny, nx))
        if 0 <= ny < n and 0 <= nx < m and answer[ny][nx] != -1:
            if cnt > answer[ny][nx] + 1:
                cnt = answer[ny][nx] + 1
    answer[y][x] = cnt

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            answer[i][j] = 0

for i in range(n):
    for j in range(m):
        print(answer[i][j], end=' ')
    print()
