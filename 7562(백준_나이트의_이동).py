from collections import deque
import sys

input = sys.stdin.readline
t = int(input())

dy = [-1, 1, -2, 2, -2, 2, -1, 1]
dx = [-2, -2, -1, -1, 1, 1, 2, 2]

for _ in range(t):
    length = int(input())
    sy, sx = map(int, input().split())
    ey, ex = map(int, input().split())
    q = deque()
    q.append((sy, sx, 0))
    visited = [[0] * length for _ in range(length)]
    while q:
        y, x, cnt = q.popleft()
        if not (0 <= y < length and 0 <= x < length and visited[y][x] == 0):
            continue
        if (y, x) == (ey, ex):
            print(cnt)
            break
        visited[y][x] = 1
        for i in range(8):
            q.append((y + dy[i], x + dx[i], cnt + 1))
