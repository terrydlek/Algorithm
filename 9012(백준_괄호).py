import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    string = input().strip()
    stack = []
    for i in string:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                print('NO')
                break
            stack.pop()
    else:
        if not stack:
            print('YES')
        else:
            print('NO')
