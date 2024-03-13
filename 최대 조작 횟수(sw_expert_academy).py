t = int(input())

tc = [list(map(int, input().split())) for _ in range(t)]

for i, j in enumerate(tc):
    num = j[1] - j[0]
    if num == 0:
        print(f'#{i + 1} {0}')
    elif num == 1 or num < 0:
        print(f'#{i + 1} {-1}')
    else:
        result = 0
        if num % 2 != 0:
            result += 1
            num -= 3
        result += num // 2
        print(f'#{i + 1} {result}')
