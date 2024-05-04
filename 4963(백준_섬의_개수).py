import sys
from collections import deque
input = sys.stdin.readline

dy = [1, -1, 0, 0, -1, -1, 1, 1]
dx = [0, 0, 1, -1, -1, 1, -1, 1]

while True:
    w, h = map(int, input().split())
    if (w, h) == (0, 0):
        break
    graph = []
    for _ in range(h):
        graph.append(list(map(int, input().split())))
    answer = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] != 0:
                q = deque()
                q.append((i, j))
                while q:
                    y, x = q.popleft()
                    if not (0 <= y < h and 0 <= x < w and graph[y][x] != 0):
                        continue
                    graph[y][x] = 0
                    for k in range(8):
                        q.append((y + dy[k], x + dx[k]))
                answer += 1
    print(answer)
