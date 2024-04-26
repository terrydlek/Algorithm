import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
avail = []
for _ in range(n):
    avail.append(input().strip().split())
q = deque()
for i in avail:
    if i[0] == 'push':
        q.append(i[1])
    elif i[0] == 'pop':
        if not q:
            print(-1)
        else:
            print(q.popleft())
    elif i[0] == 'size':
        print(len(q))
    elif i[0] == 'empty':
        if not q:
            print(1)
        else:
            print(0)
    elif i[0] == 'front':
        if not q:
            print(-1)
        else:
            print(q[0])
    elif i[0] == 'back':
        if not q:
            print(-1)
        else:
            print(q[-1])