n, m = map(int, input().split())

ali = list(list(input()) for _ in range(n))
bli = list(list(input()) for _ in range(n))


def change(y, x):
    for i in range(y, y + 3):
        for j in range(x, x + 3):
            if ali[i][j] == '0':
                ali[i][j] = '1'
            else:
                ali[i][j] = '0'


answer = 0
y, x = 0, 0
while y < n - 2:
    while x < m - 2:
        if ali[y][x] != bli[y][x]:
            answer += 1
            change(y, x)
        x += 1
    y += 1
    x = 0

if ali != bli:
    print(-1)
else:
    print(answer)
