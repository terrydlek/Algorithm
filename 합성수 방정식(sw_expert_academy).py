tc = int(input())


def check_hs(n):
    if n**0.5 == int(n**0.5):
        return True
    for i in range(2, n):
        if n % i == 0:
            return True
    return False


for i in range(tc):
    n = int(input())
    cur = 4
    while True:
        if check_hs(cur) and check_hs(cur + n):
            break
        cur += 1
    print(f'#{i + 1} {cur + n} {cur}')
