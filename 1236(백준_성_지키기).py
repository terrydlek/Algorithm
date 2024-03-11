n, m = map(int, input().split())

state = [list(map(str, input())) for _ in range(n)]
rstate = []
for i in range(m):
    li = []
    for j in range(n):
        li.append(state[j][i])
    rstate.append(li)

answer = 0

for i in range(n):
    if 'X' not in state[i]:
        check = []
        for j in range(m):
            if 'X' not in rstate[j]:
                check.append((i, j))
        if not check:
            state[i][j] = 'X'
            rstate[j][i] = 'X'
        else:
            y, x = check[0]
            state[y][x] = 'X'
            rstate[x][y] = 'X'
        answer += 1

for i in range(m):
    if 'X' not in rstate[i]:
        check = []
        for j in range(n):
            if 'X' not in state[j]:
                check.append((i, j))
        if not check:
            rstate[i][j] = 'X'
            state[j][i] = 'X'
        else:
            y, x = check[0]
            rstate[y][x] = 'X'
            state[x][y] = 'X'
        answer += 1


print(answer)
