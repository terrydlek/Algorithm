import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())

miro = [list(input().strip()) for _ in range(n)]

q = deque()
q.append((0, 0, 1))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
answer = 0
while q:
    y, x, cnt = q.popleft()
    if not (0 <= y < n and 0 <= x < m and miro[y][x] == '1'):
        continue
    miro[y][x] = '0'
    if (y, x) == (n - 1, m - 1):
        answer = cnt
        continue
    for i in range(4):
        q.append((y + dy[i], x + dx[i], cnt + 1))

print(answer)
