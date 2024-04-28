import sys
import heapq
input = sys.stdin.readline

q = []

n = int(input())
avail = []
for _ in range(n):
    num = int(input())
    if num == 0:
        if not q:
            print(0)
        else:
            print(heapq.heappop(q))
    else:
        heapq.heappush(q, num)
