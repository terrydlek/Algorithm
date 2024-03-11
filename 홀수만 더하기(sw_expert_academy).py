t = int(input())

case = []
for _ in range(t):
    li = list(map(int, input().split()))
    case.append(li)

for k, i in enumerate(case):
    total = 0
    for j in i:
        if j % 2 == 1:
            total += j
    print('#{} {}'.format(k + 1, total))