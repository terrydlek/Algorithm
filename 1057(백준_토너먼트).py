n, kim, im = map(int, input().split())

answer = 1

cnt = 0
while (kim - 1) // 2 != (im - 1) // 2:
    kim = (kim - 1) // 2 + 1
    im = (im - 1) // 2 + 1
    answer += 1

print(answer)
