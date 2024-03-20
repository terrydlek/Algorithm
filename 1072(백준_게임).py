x, y = map(int, input().split())
crt = y * 100 // x
if crt >= 99:
    print(-1)
else:
    answer = x
    s, e = 0, x
    while s <= e:
        m = (s + e) // 2
        if (y + m) * 100 // (x + m) > crt:
            answer = m
            e = m - 1
        else:
            s = m + 1
    print(answer)
