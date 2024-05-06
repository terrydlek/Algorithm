import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    maxq = []
    minq = []
    dic = defaultdict(int)
    for _ in range(n):
        oper, num = input().strip().split()
        if oper == 'I':
            heapq.heappush(maxq, (int(num) * -1, int(num)))
            heapq.heappush(minq, int(num))
            dic[int(num)] += 1
        else:
            if maxq and minq:
                if num == '1':
                    while maxq:
                        a = heapq.heappop(maxq)
                        if a[1] in dic and dic[a[1]] != 0:
                            dic[a[1]] -= 1
                            if dic[a[1]] == 0:
                                del dic[a[1]]
                            break
                else:
                    while minq:
                        a = heapq.heappop(minq)
                        if a in dic and dic[a] != 0:
                            dic[a] -= 1
                            if dic[a] == 0:
                                del dic[a]
                            break
        # print(maxq, minq, dic)

    if not dic:
        print('EMPTY')
    else:
        li = sorted(dic)
        print(f'{li[-1]} {li[0]}')
