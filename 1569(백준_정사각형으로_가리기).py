spot = []
mnx, mxx, mny, mxy = 1e9, -1e9, 1e9, -1e9

for _ in range(int(input())):
    x, y = map(int, input().split())
    if x < mnx: mnx = x
    if x > mxx: mxx = x
    if y < mny: mny = y
    if y > mxy: mxy = y
    spot.append([x, y])

length = max(mxx - mnx, mxy - mny)
cnt1, cnt2 = 0, 0
for i in spot:
    x, y = i
    if x in (mnx, mnx + length):
        if mny <= y <= mny + length:
            cnt1 += 1
    elif y in (mny, mny + length):
        if mnx <= x <= mnx + length:
            cnt1 += 1

for i in spot:
    x, y = i
    if x in (mxx, mxx - length):
        if mxy - length <= y <= mxy:
            cnt2 += 1
    elif y in (mxy, mxy - length):
        if mxx - length <= x <= mxx:
            cnt2 += 1

if len(spot) not in (cnt1, cnt2):
    print(-1)
else:
    print(length)
