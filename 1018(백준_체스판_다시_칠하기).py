n, m = map(int, input().split())

chess = []

for _ in range(n):
    chess.append(input())

avail = ['WB', 'BW']

wf, bf = [], []

cur = 0
for _ in range(8):
    wf.append(avail[cur] * 4)
    cur = (cur + 1) % 2

cur = 1
for _ in range(8):
    bf.append(avail[cur] * 4)
    cur = (cur + 1) % 2

answer = 1e9
cur = 0
for i in range(0, n - 7):
    for j in range(0, m - 7):
        cw, cb = 0, 0
        for k in range(8):
            for ori, new in zip(wf[k], chess[i + k][j:j + 8]):
                if ori != new:
                    cw += 1

        for k in range(8):
            for ori, new in zip(bf[k], chess[i + k][j:j + 8]):
                if ori != new:
                    cb += 1

        if answer > min(cw, cb):
            answer = min(cw, cb)
        if answer == 0:
            break
    if answer == 0:
        break
print(answer)
