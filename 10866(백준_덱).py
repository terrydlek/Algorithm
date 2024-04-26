import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
avail = []
for _ in range(n):
    avail.append(list(map(str, input().strip().split())))

deque = deque()

for i in avail:
    if i[0] == 'push_front':
        deque.appendleft(i[1])
    elif i[0] == 'push_back':
        deque.append(i[1])
    elif i[0] == 'pop_front':
        if not deque:
            print(-1)
        else:
            print(deque.popleft())
    elif i[0] == 'pop_back':
        if not deque:
            print(-1)
        else:
            print(deque.pop())
    elif i[0] == 'size':
        print(len(deque))
    elif i[0] == 'empty':
        if not deque:
            print(1)
        else:
            print(0)
    elif i[0] == 'front':
        if not deque:
            print(-1)
        else:
            print(deque[0])
    elif i[0] == 'back':
        if not deque:
            print(-1)
        else:
            print(deque[-1])
