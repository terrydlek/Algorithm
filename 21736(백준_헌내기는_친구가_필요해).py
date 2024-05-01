import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
cam = []
for _ in range(n):
    cam.append(list(input().strip()))

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

starty, startx = 0, 0
for i in range(n):
    for j in range(m):
        if cam[i][j] == 'I':
            starty, startx = i, j

q = deque()
q.append((starty, startx))

answer = 0

while q:
    y, x = q.popleft()
    if not (0 <= y < n and 0 <= x < m and cam[y][x] != 0 and cam[y][x] != 'X'):
        continue
    if cam[y][x] == 'P':
        answer += 1
    cam[y][x] = 0
    for i in range(4):
        q.append((y + dy[i], x + dx[i]))

if answer == 0:
    print('TT')
else:
    print(answer)
