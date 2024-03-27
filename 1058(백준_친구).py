n = int(input())

friends = list(list(input()) for _ in range(n))

answer = [0] * n

for i in range(n):
    cnt = []
    for j in range(n):
        if friends[i][j] == 'Y':
            if j not in cnt:
                cnt.append(j)
            for k in range(n):
                if friends[j][k] == 'Y' and k not in cnt and i != k:
                    cnt.append(k)
    answer[i] = len(cnt)

print(max(answer))
