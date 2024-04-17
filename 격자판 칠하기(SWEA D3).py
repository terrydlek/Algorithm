from collections import deque
t = int(input())


def dfs(ny, nx, grph):
    q = deque()
    q.append((ny, nx, -1, -1))
    visited = [[0] * m for _ in range(n)]
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    while q:
        y, x, prvy, prvx = q.popleft()
        if not (0 <= y < n and 0 <= x < m and visited[y][x] == 0):
            continue
        visited[y][x] = 1
        if (prvy, prvx) != (-1, -1):
            if grph[prvy][prvx] == '#':
                if grph[y][x] == '?' or grph[y][x] == '.':
                    grph[y][x] = '.'
                else:
                    return False
            elif grph[prvy][prvx] == '.':
                if grph[y][x] == '?' or grph[y][x] == '#':
                    grph[y][x] = '#'
                else:
                    return False
        for i in range(4):
            q.append((y + dy[i], x + dx[i], y, x))
    return True


for tc in range(1, t + 1):
    n, m = map(int, input().split())
    px = [list(input()) for _ in range(n)]
    starty, startx = -1, -1
    for yy in range(n):
        for xx in range(m):
            if px[yy][xx] in ('#', '.'):
                starty, startx = yy, xx
                break
        if (starty, startx) != (-1, -1):
            break
    if (starty, startx) != (-1, -1):
        if dfs(starty, startx, px):
            print(f'#{tc} {"possible"}')
        else:
            print(f'#{tc} {"impossible"}')
    else:
        print(f'#{tc} {"possible"}')
