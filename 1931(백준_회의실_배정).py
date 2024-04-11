import sys
input = sys.stdin.readline
time = []
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    time.append([a, b])

time = sorted(time, key=lambda x:(x[1], x[0]))

avail = []
for i in time:
    if not avail:
        avail.append(i[1])
    else:
        if avail[-1] <= i[0]:
            avail.append(i[1])

print(len(avail))
