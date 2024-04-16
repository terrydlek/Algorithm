import math
t = int(input())

for tc in range(1, t + 1):
    num = list(map(int, input().split()))
    answer = sum(num) / len(num)
    print(f'#{tc} {int(round(answer, 0))}')
