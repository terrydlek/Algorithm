import sys
from collections import Counter
input = sys.stdin.readline
n = int(input())
avail = []
for _ in range(n):
    avail.append(int(input()))
avail.sort()
print(int(round(sum(avail) / len(avail), 0)))
print(avail[len(avail) // 2])
cnt = Counter(avail)
cnt = sorted(cnt.items(), key=lambda x: x[1], reverse=True)
if len(cnt) == 1 or cnt[0][1] != cnt[1][1]:
    print(cnt[0][0])
else:
    print(cnt[1][0])
print(avail[-1] - avail[0])
