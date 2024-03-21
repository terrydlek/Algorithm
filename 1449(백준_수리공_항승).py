from collections import deque
n, l = map(int, input().split())
idx = list(map(int, input().split()))

idx.sort()
q = deque(idx)

answer = 0
cur = -1
while q:
    a = q.popleft()
    if cur >= a + 0.5:
        continue
    answer += 1
    cur = a - 0.5 + l
print(answer)
