t = int(input())

for tc in range(1, t + 1):
    check = input()
    if check.count('o') + (15 - len(check)) >= 8:
        print(f'#{tc} {"YES"}')
    else:
        print(f'#{tc} {"NO"}')
