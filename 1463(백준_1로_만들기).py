import sys
n = int(sys.stdin.readline())

avail = [0] * (10**6 + 1)

for i in range(2, n + 1):
    avail[i] = avail[i - 1] + 1
    if i % 2 == 0:
        avail[i] = min(avail[i], avail[i // 2] + 1)
    if i % 3 == 0:
        avail[i] = min(avail[i], avail[i // 3] + 1)
print(avail[n])
