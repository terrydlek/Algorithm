import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
grph = [list(map(int, input().split())) for _ in range(n)]

answer = 1


def dfs(visited, n):
    q = deque()
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                q.append((i, j))
                while q:
                    y, x = q.popleft()
                    if not (0 <= y < n and 0 <= x < n and visited[y][x] == 0):
                        continue
                    visited[y][x] = 1

                    for k in range(4):
                        q.append((y + dy[k], x + dx[k]))

                cnt += 1
    return cnt


for i in range(1, 100 + 1):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    cnt = 0
    for j in range(n):
        for k in range(n):
            if grph[j][k] <= i:
                visited[j][k] = 1
                cnt += 1
    if cnt == n * n:
        break

    cnt = dfs(visited, n)
    if answer < cnt:
        answer = cnt
print(answer)
