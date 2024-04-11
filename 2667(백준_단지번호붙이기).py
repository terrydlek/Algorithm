from collections import deque
n = int(input())
danji = [list(input()) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
q = deque()
answer1 = 0
li = []
for i in range(n):
    for j in range(n):
        if danji[i][j] != '0':
            answer1 += 1
            q.append((i, j))
            answer2 = 0
            while q:
                y, x = q.popleft()
                if not (0 <= y < n and 0 <= x < n and danji[y][x] != '0'):
                    continue
                danji[y][x] = '0'
                answer2 += 1
                for k in range(4):
                    q.append((y + dy[k], x + dx[k]))
            li.append(answer2)

li.sort()
print(answer1)
for i in li:
    print(i)
