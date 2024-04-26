import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

q = deque([i for i in range(1, n + 1)])
answer = []
cnt = 0

while q:
    cnt += 1
    a = q.popleft()
    if cnt == k:
        answer.append(str(a))
        cnt = 0
    else:
        q.append(a)

answer = ', '.join(answer)
print(f'<{answer}>')
