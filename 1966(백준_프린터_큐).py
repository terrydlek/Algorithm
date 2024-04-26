import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
for _ in range(n):
    n, m = map(int, input().split())
    prior = deque(list(map(int, input().split())))
    # print(n, m)
    # print(prior)
    # print('-------------')
    answer = 1
    while prior:
        rank = prior.popleft()
        if not prior or rank >= max(prior):
            if m == 0:
                print(answer)
                break
            else:
                answer += 1
                m -= 1
        else:
            prior.append(rank)
            if m == 0:
                m = len(prior) - 1
            else:
                m -= 1