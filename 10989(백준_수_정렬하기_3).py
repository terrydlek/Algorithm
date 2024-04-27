import sys
input = sys.stdin.readline

n = int(input())
num = [0] * (10001)
for _ in range(n):
    n = int(input())
    num[n] += 1

for i, j in enumerate(num):
    if j != 0:
        for _ in range(j):
            print(i)
