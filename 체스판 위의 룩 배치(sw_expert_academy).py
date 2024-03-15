t = int(input())

for i in range(t):
    li = [list(map(str, input())) for _ in range(8)]

    row, col = [], []
    cnt = 0
    answer = ['yes', 'no']
    for j in range(8):
        for k in range(8):
            if li[j][k] == 'O':
                if k in row or j in col or cnt > 8:
                    cnt = -1
                    break
                row.append(k)
                col.append(j)
                cnt += 1
        if cnt == -1:
            print(f'#{i + 1} {answer[1]}')
            break
    else:
        if cnt == 8:
            print(f'#{i + 1} {answer[0]}')
        else:
            print(f'#{i + 1} {answer[1]}')