t = int(input())

for tc in range(1, t + 1):
    a, b, c = map(int, input().split())
    answer = 0
    candy = [c, b, a]
    for i in range(1, 3):
        if candy[i - 1] <= candy[i]:
            answer += candy[i] - candy[i - 1] + 1
            candy[i] -= candy[i] - candy[i - 1] + 1
    for i in candy:
        if i <= 0:
            print(f'#{tc} {-1}')
            break
    else:
        print(f'#{tc} {answer}')
