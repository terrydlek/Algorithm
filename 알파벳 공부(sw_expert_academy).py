t = int(input())

dic = {i: j for i, j in zip('abcdefghijklmnopqrstuvwxyz', range(1, 27))}

for i in range(1, t + 1):
    string = input()
    cnt = 0
    for j, k in enumerate(string):
        if dic[k] == j + 1:
            cnt += 1
        else:
            break

    print(f'#{i} {cnt}')
