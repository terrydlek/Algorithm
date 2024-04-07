import sys
input = sys.stdin.readline
n = int(input())

words = []
for _ in range(n):
    words.append(input().rstrip())

words = sorted(words)
stack = []
for i in words:
    if not stack or stack[-1] != i[:len(stack[-1])]:
        stack.append(i)
    else:
        stack.pop()
        stack.append(i)

print(len(stack))
