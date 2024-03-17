a, b = map(str, input().split())
avail = [i for i in range(len(b) - len(a) + 1)]

answer = 1e9
for i in avail:
    cnt = 0
    for j, k in zip(a, b[i:i + len(a)]):
        if j != k:
            cnt += 1
    if answer > cnt:
        answer = cnt
print(answer)
