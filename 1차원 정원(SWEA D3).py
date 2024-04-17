t = int(input())

for tc in range(1, t + 1):
    n, d = map(int, input().split())
    answer = 1
    cur = d
    while cur + d < n - 1:
        cur += (d * 2 + 1)
        answer += 1
    print(f'#{tc} {answer}')
