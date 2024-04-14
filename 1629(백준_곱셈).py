import sys
input = sys.stdin.readline
a, b, c = map(int, input().split())


def cal(a, b, c):
    if b == 1:
        return a % c
    temp = cal(a, b // 2, c)
    if b % 2 == 0:
        return (temp * temp) % c
    else:
        return (temp * temp * a) % c


print(cal(a, b, c))
