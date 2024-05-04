import sys
input = sys.stdin.readline

prime = [0 for _ in range(123456 * 2 + 1)]
prime[1] = 1
prime[2] = 0

for i in range(2, len(prime)):
    if prime[i] == 0:
        for j in range(i * i, len(prime), i):
            prime[j] = 1

while True:
    n = int(input())
    if n != 0:
        print(prime[n+1 : 2*n+1].count(0))
    else:
        break
