tc = int(input())


def check_pel(string):
    if list(string) == list(reversed(string)):
        return True
    return False


def check_pair(li, string):
    if ''.join(list(reversed(string))) in li and li[li.index(string)] != li[li.index(''.join(list(reversed(string))))]:
        return True
    return False


for i in range(1, tc + 1):
    n, m = map(int, input().split())

    li = []
    for _ in range(n):
        li.append(input())

    # 쌍이 있는 단어는 pair에
    pair = []
    # 쌍이 없는 pel은 alone에
    alone = []

    for j in li:
        if j == '0':
            continue

        if check_pair(li, j):
            pair.append(2)
            li[li.index(j)] = '0'
            li[li.index(''.join(list(reversed(j))))] = '0'

        elif check_pel(j):
            alone.append(1)
            li[li.index(j)] = '0'

    if alone:
        print(f'#{i} {sum(pair) * m + alone[0] * m}')
    else:
        print(f'#{i} {sum(pair) * m}')
