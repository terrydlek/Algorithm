l = int(input())
li = list(map(int, input().split()))
n = int(input())


if n in li:
    print(0)
else:
    li = sorted(li)
    start, end = 0, 0
    for i, j in enumerate(li):
        if j > n:
            if i != 0:
                start, end = li[i - 1] + 1, li[i] - 1
            else:
                start = 1
                end = li[0] - 1
            break
    print((end - n + 1) * (n - start) + (end - n))
