for _ in range(1, 11):
    tc = int(input())
    li = [list(map(int, input().split())) for _ in range(100)]
    row = []
    for i in range(100):
        row.append(sum(li[i]))
    col = [0] * (100)
    for i in range(100):
        for j in range(100):
            col[j] += li[i][j]
    crss = [0, 0]
    y, x = 0, 0
    while y < 100 and x < 100:
        crss[0] += li[y][x]
        x += 1
        y += 1
    y, x = 99, 99
    while y >= 0 and x >= 0:
        crss[1] += li[y][x]
        x -= 1
        y -= 1
    print(f'#{tc} {max(row + col + crss)}')
