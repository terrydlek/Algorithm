import sys
input = sys.stdin.readline

n = int(input())
avail = []
for _ in range(n):
    avail.append(input().strip().split())
stack = []

for i in avail:
    if i[0] == 'push':
        stack.append(i[1])
    elif i[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print('-1')
    elif i[0] == 'size':
        print(len(stack))
    elif i[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif i[0] == 'top':
        if not stack:
            print(-1)
        else:
            print(stack[-1])
