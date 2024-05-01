import sys
from itertools import combinations as cb
input = sys.stdin.readline

t = int(input())
for _ in range(t):

    n = int(input())
    student = list(map(str, input().strip().split()))

    if n > 32:
        print(0)
    else:
        answer = 1e9
        for i in cb(student, 3):
            cnt = 0
            for j in range(3):
                for k in range(j + 1, 3):
                    for one, two in zip(i[j], i[k]):
                        if one != two:
                            cnt += 1
            if answer > cnt:
                answer = cnt
        print(answer)
