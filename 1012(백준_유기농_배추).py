from collections import deque
t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())
    farm = [[0] * m for _ in range(n)]
    answer = 0
    for i in range(k):
        a, b = map(int, input().split())
        farm[b][a] = 1

    for i in range(n):
        for j in range(m):
            if farm[i][j] == 1:
                q = deque()
                q.append((i, j))
                while q:
                    y, x = q.popleft()
                    if not (0 <= y < n and 0 <= x < m) or farm[y][x] == 0 or farm[y][x] == -1:
                        continue
                    if farm[y][x] == 1:
                        farm[y][x] = -1
                    q.append((y - 1, x))
                    q.append((y + 1, x))
                    q.append((y, x - 1))
                    q.append((y, x + 1))
                answer += 1
    print(answer)
