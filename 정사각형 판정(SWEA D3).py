t = int(input())


def check(y, x, length):
    if y + length <= len(px) and x + length <= len(px[0]):
        for yy in range(y, y + length):
            for xx in range(x, x + length):
                if px[yy][xx] != '#':
                    return False
        return True
    return False


for tc in range(1, t + 1):
    n = int(input())
    px = [input() for _ in range(n)]
    cnt = 0
    for i in px:
        cnt += i.count('#')
    length = int(cnt**0.5)
    if length != cnt**0.5:
        print(f'#{tc} {"no"}')
    else:
        state = False
        for i in range(len(px)):
            for j in range(len(px[0])):
                if check(i, j, length):
                    state = True
                    break
            if state:
                print(f'#{tc} {"yes"}')
                break
        else:
            print(f'#{tc} {"no"}')
