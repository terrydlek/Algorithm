import sys
from itertools import product
input = sys.stdin.readline

n = int(input())
m = int(input())
failure = []
if m != 0:
    failure = list(map(int, input().split()))

avail = [i for i in range(10) if i not in failure]


if abs(n - 100) <= 3:
    print(abs(n - 100))
else:
    answer = abs(n - 100)
    for i in range(1, len(str(n)) + 2):
        for j in product(avail, repeat=i):
            tt = i
            string = ''
            for k in j:
                string += str(k)
            tt = i + abs(n - int(string))
            if answer > tt:
                answer = tt
    print(answer)
