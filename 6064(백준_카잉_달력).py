import sys
input = sys.stdin.readline

t = int(input())


def cal(m, n, x, y):
    answer = x
    while answer <= m * n:
        if (answer - x) % m == 0 and (answer - y) % n == 0:
            return answer
        answer += m
    return -1


for _ in range(t):
    m, n, x, y = map(int, input().split())
    print(cal(m, n, x, y))
