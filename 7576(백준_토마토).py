import sys
from collections import deque
input = sys.stdin.readline
m, n = map(int, input().split())
mato = [list(map(int, input().split())) for _ in range(n)]

a = set()
for i in range(n):
    for j in range(m):
        if mato[i][j] == 1:
            a.add((i, j))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

answer = 0
while True:
     nw = set()
     for i in a:
         y, x = i
         for j in range(4):
             ny = y + dy[j]
             nx = x + dx[j]
             if 0 <= ny < n and 0 <= nx < m and mato[ny][nx] == 0:
                 mato[ny][nx] = 1
                 nw.add((ny, nx))
     if not nw:
         break
     answer += 1
     a = nw

for i in mato:
    if 0 in i:
        print(-1)
        break
else:
    print(answer)
