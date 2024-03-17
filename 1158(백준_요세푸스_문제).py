from collections import deque

n, k = map(int, input().split())

q = deque([i + 1 for i in range(n)])
cnt = 0
result = []
while q:
    cnt += 1
    a = q.popleft()
    if cnt != k:
        q.append(a)
    else:
        result.append(a)
        cnt = 0

answer = '<'
for i, j in enumerate(result):
    if i != n - 1:
        answer += str(j) + ', '
    else:
        answer += str(j) + '>'
print(answer)