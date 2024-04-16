t = int(input())

for tc in range(1, t + 1):
    a, b = map(int, input().split())
    string = ''
    if a > b:
        string = '>'
    elif a == b:
        string = '='
    else:
        string = '<'
    print(f'#{tc} {string}')
