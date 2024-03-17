bd = input()

answer = ''
cnt = 0
for i in bd:
    if i == 'X':
        cnt += 1
    else:
        if cnt % 2 != 0:
            print(-1)
            break
        answer += 'AAAA' * (cnt // 4) + 'BB' * ((cnt % 4) // 2) + '.'
        cnt = 0
else:
    answer += 'AAAA' * (cnt // 4) + 'BB' * ((cnt % 4) // 2)
    if cnt % 2 != 0:
        print(-1)
    else:
        print(answer)
