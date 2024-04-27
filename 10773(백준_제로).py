import sys
input = sys.stdin.readline

k = int(input())
avail = []
for _ in range(k):
    n = int(input())
    avail.append(n)

stack = []
for i in avail:
    if i != 0:
        stack.append(i)
    else:
        stack.pop()
print(sum(stack))
