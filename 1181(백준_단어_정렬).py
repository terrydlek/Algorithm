import sys
input = sys.stdin.readline

n = int(input())

alpha = set()
for _ in range(n):
    alpha.add(input().strip())

alpha = sorted(alpha, key=lambda x: (len(x), x))
for i in alpha:
    print(i)