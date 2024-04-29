import sys
input = sys.stdin.readline

n = int(input())
avail = list(map(int, input().split()))
srt = sorted(avail)

dic = dict()
cnt = 0
for i in srt:
    if i not in dic:
        dic[i] = cnt
        cnt += 1

for i in avail:
    print(dic[i], end=' ')
