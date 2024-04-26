import sys
input = sys.stdin.readline

start, end = map(int, input().split())
mx = 1000000
prime = [1] * (mx + 1)
prime[0], prime[1] = 0, 0

for i in range(int(mx**0.5) + 1):
    if prime[i] == 0:
        continue
    for j in range(i*i, mx, i):
        prime[j] = 0

for i in range(start, end + 1):
    if prime[i] == 1:
        print(i)
