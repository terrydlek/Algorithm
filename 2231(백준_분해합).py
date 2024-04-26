import sys
input = sys.stdin.readline

n = int(input())

cnt = 1
while cnt < n:
    total = cnt
    for i in str(cnt):
        total += int(i)
    if total == n:
        print(cnt)
        break
    cnt += 1
else:
    print(0)
    