import sys
input = sys.stdin.readline


prime = [0] * (10001)
prime[0], prime[1] = 1, 1
for i in range(2, 10001):
    if prime[i] == 0:
        for j in range(i*i, 10001, i):
            prime[j] = 1

for _ in range(int(input())):
    n = int(input())
    x, y = n // 2, n // 2
    while (prime[x], prime[y]) != (0, 0):
        x -= 1
        y += 1
    print(x, y)
