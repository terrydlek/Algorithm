import sys
input = sys.stdin.readline

n = int(input())
stack, maxnum, answer = [], 0, ''

avail = []
for _ in range(n):
    avail.append(int(input()))

for n in avail:
    if maxnum < n:
        if not stack:
            maxnum += 1
            stack.append(maxnum)
            answer += '+'
        while stack[-1] != n:
            maxnum += 1
            stack.append(maxnum)
            answer += '+'
        stack.pop()
        answer += '-'
    else:
        if not stack or stack[-1] != n:
            print('NO')
            break
        else:
            stack.pop()
            answer += '-'
else:
    for i in answer:
        print(i)
