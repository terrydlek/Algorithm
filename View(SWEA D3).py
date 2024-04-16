for tc in range(1, 11):
    n = int(input())
    building = list(map(int, input().split()))
    answer = 0
    for i in range(2, n - 2):
        lrmax = max([building[i - 1], building[i - 2], building[i + 1], building[i + 2]])
        if building[i] > lrmax:
            answer += building[i] - lrmax
    print(f'#{tc} {answer}')
