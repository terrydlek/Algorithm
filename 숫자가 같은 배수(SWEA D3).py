from itertools import permutations as pt
t = int(input())

for tc in range(1, t + 1):
    num = int(input())
    for i in pt(str(num), len(str(num))):
        a = int(''.join(list(i)))
        if a > num and a % num == 0:
            print(f'#{tc} {"possible"}')
            break
    else:
        print(f'#{tc} {"impossible"}')
        