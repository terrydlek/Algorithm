n, m = map(int, input().split())
rect = [list(map(str, input())) for _ in range(n)]


def check(y, x, plus):
    pl = plus - 1
    if y + pl >= n or x + pl >= m:
        return False
    one = rect[y][x]
    two = rect[y][x + pl]
    three = rect[y + pl][x]
    four = rect[y + pl][x + pl]
    if one == two and one == three and one == four:
        return True
    return False


plus = min(n, m)
while plus != -1:
    for i in range(n):
        for j in range(m):
            if check(i, j, plus):
                print(plus**2)
                plus = -1
                break
        if plus == -1:
            break
    if plus != -1:
        plus -= 1
