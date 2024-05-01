import sys
input = sys.stdin.readline

n, k = map(int, input().split())

avail = []
for _ in range(n):
    avail.append(int(input()))

answer = 0
for i in sorted(avail, reverse=True):
    answer += k // i
    k %= i
print(answer)
