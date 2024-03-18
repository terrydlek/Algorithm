n, m = map(int, input().split())
avail = []
for _ in range(m):
    avail.append(int(input()))

avail.sort()

total = -1
price = -1
for i in range(len(avail)):
    ttprice = avail[i:i + n][0] * len(avail[i:i + n])
    if total < ttprice:
        total = ttprice
        price = avail[i:i + n][0]
print(price, total)
