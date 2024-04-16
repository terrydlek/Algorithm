import sys
input = sys.stdin.readline

primes = [1] * (1000001)
primes[0], primes[1] = 0, 0
for i in range(2, 1000001):
    if primes[i]:
        for j in range(2 * i, 1000001, i):
            primes[j] = 0

while True:
    n = int(input())
    if n == 0:
        break
    for i in range(3, n // 2 + 1, 2):
        if primes[i] and primes[n - i]:
            print(f'{n} = {i} + {n - i}')
            break
    else:
        print("Goldbach's conjecture is wrong.")
