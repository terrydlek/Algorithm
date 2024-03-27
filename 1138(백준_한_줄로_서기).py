n = int(input())
remember = list(map(int, input().split()))

answer = [0] * n
for idx, rem in enumerate(remember):
    cnt = 0
    for j in range(n):
        if answer[j] == 0:
            cnt += 1
            if cnt > rem:
                answer[j] = idx + 1
                break

for i in answer:
    print(i, end=' ')
