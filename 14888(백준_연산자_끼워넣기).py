import sys
from itertools import permutations as pt
input = sys.stdin.readline
n = int(input())
num = list(map(int, input().split()))
oper = list(map(int, input().split()))

li = ['+', '-', '*', '/']
avail = ''.join([j * i for i, j in zip(oper, li) if i != 0])
avail = list(set(pt(avail, len(avail))))

mn, mx = 1e9, -1e9
for i in range(len(avail)):
    answer = num[0]
    for j, k in zip(num[1:], avail[i]):
        if k == '/':
            k = '//'
        if k == '//' and answer < 0:
            answer = -(abs(answer) // j)
        else:
            answer = eval(str(answer) + k + str(j))
    if answer < mn:
        mn = answer
    if answer > mx:
        mx = answer

print(int(mx))
print(int(mn))
