tc = int(input())

for cnt in range(1, tc + 1):
    n = int(input())
    li = list(map(int, input().split()))

    answer = []

    cp = li.copy()

    for i in range(len(li)):
        if cp[i] != 0 and li[i] * 4 / 3 in cp:
            answer.append(str(li[i]))
            cp[cp.index(li[i] * 4 // 3)] = 0
            # print(li, cp, i)
    # print(answer)
    answer = ' '.join(answer)
    print(f'#{cnt} {answer}')
