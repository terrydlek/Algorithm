import sys
s = list(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline())

stack = []

curidx = len(s)

for _ in range(m):
    string = sys.stdin.readline().rstrip()
    # print(s, string)
    if string == 'L':
        if s:
            stack.append(s.pop())
    elif string == 'D':
        if stack:
            s.append(stack.pop())
    elif string == 'B':
        if s:
            s.pop()
    else:
        s.append(string[-1])
    # print(s, stack)
    # print('-----------------')
s += stack[::-1]
print(''.join(s))
