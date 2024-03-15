t = int(input())

for i in range(1, t + 1):
    string = input()
    cnt = string.count('|)') + string.count('(|') + string.count('()')
    print(f'#{i} {cnt}')
