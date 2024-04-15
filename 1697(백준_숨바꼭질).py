import sys
from collections import deque
input = sys.stdin.readline
n, k = map(int, input().split())

answer = 0
if n >= k:
    answer = n - k
else:
    visited = [1e9] * (200001)
    q = deque()
    q.append((n, 0))
    visited[n] = 0
    while q:
        idx, cnt = q.popleft()
        if idx > 200001 or idx < 0 or visited[idx] < cnt:
            continue
        visited[idx] = cnt
        if idx == k:
            break
        if idx > k:
            q.append((idx - 1, cnt + 1))
        else:
            q.append((idx + 1, cnt + 1))
            q.append((idx - 1, cnt + 1))
            q.append((idx * 2, cnt + 1))
    answer = visited[k]

print(answer)
