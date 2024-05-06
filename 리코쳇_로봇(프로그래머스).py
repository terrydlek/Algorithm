import sys
from collections import deque

input = sys.stdin.readline

# 보드의 행, 열 입력받기
n, m = map(int, input().split())

board = [input().strip() for _ in range(n)]


def solution(board):
    answer = 0
    sy, sx = 0, 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                sy, sx = i, j
                break

    def right(board, y, x):
        dy, dx = y, x
        while 0 <= dy < len(board) and 0 <= dx + 1 < len(board[0]) and board[dy][dx + 1] != 'D':
            dx += 1
        return (dy, dx)

    def left(board, y, x):
        dy, dx = y, x
        while 0 <= dy < len(board) and 0 <= dx - 1 < len(board[0]) and board[dy][dx - 1] != 'D':
            dx -= 1
        return (dy, dx)

    def up(board, y, x):
        dy, dx = y, x
        while 0 <= dy - 1 < len(board) and 0 <= dx < len(board[0]) and board[dy - 1][dx] != 'D':
            dy -= 1
        return (dy, dx)

    def down(board, y, x):
        dy, dx = y, x
        while 0 <= dy + 1 < len(board) and 0 <= dx < len(board[0]) and board[dy + 1][dx] != 'D':
            dy += 1
        return (dy, dx)

    visited = []
    q = deque()
    q.append((sy, sx, 0))

    while q:
        y, x, cnt = q.popleft()
        if board[y][x] == 'G':
            answer = cnt
            break
        if (y, x, 'r') not in visited:
            visited.append((y, x, 'r'))
            a, b = right(board, y, x)
            if (a, b) != (y, x):
                q.append((a, b, cnt + 1))
        if (y, x, 'l') not in visited:
            visited.append((y, x, 'l'))
            a, b = left(board, y, x)
            if (a, b) != (y, x):
                q.append((a, b, cnt + 1))
        if (y, x, 'u') not in visited:
            visited.append((y, x, 'u'))
            a, b = up(board, y, x)
            if (a, b) != (y, x):
                q.append((a, b, cnt + 1))
        if (y, x, 'd') not in visited:
            visited.append((y, x, 'd'))
            a, b = down(board, y, x)
            if (a, b) != (y, x):
                q.append((a, b, cnt + 1))
    if answer == 0:
        answer = -1
    return answer


print(solution(board))
