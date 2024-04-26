import sys
input = sys.stdin.readline

n = int(input())
avail = list(map(int, input().split()))

mx = 1000
prime = [1] * (mx + 1)
prime[0], prime[1] = 0, 0

for i in range(int(mx**0.5) + 1):
    if prime[i] == 0:
        continue
    for j in range(i*i, mx + 1, i):
        prime[j] = 0

answer = 0
for i in avail:
    if prime[i] == 1:
        answer += 1
print(answer)
