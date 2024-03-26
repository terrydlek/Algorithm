n, l = map(int, input().split())
answer = []
cur = n
while cur != 0 and not answer:
    cur = n // l
    if l % 2 == 1:
        if cur - l // 2 >= 0:
            avail = [i for i in range(cur - l // 2, cur + l // 2 + 1)]
            if sum(avail) == n:
                answer = avail
                break
    else:
        if cur - l // 2 + 1 >= 0:
            avail1 = [i for i in range(cur - l // 2 + 1, cur + l // 2 +1)]
            if sum(avail1) == n:
                answer = avail1
                break
    l += 1
    if l > 100:
        break

if not answer:
    print(-1)
else:
    for i in answer:
        print(i, end=' ')
