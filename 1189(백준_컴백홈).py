import sys
input = sys.stdin.readline

r, c, k = map(int, input().split())
rd = [list(input().strip()) for _ in range(r)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

answer = 0

def dfs(x, y, cnt):
    global answer
    if cnt == k and x == 0 and y == c - 1:
        answer += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0<= ny < c and rd[nx][ny] == '.':
            rd[nx][ny] = 'T'
            dfs(nx, ny, cnt + 1)
            rd[nx][ny] = '.'


rd[r - 1][0] = 'T'
dfs(r - 1, 0, 1)
print(answer)
