import sys
input = sys.stdin.readline
n = int(input())

'''
1 - 2 - 3 - 5 - 8 - 13 - 21 - 34 - 55
'''
a, b = 1, 2

if n == 1:
    print(a)
elif n == 2:
    print(b)
else:
    for _ in range(n - 2):
        a, b = b, a + b
    print(b % 10007)
