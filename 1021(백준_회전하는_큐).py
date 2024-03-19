from collections import deque
n, m = map(int, input().split())
num = list(map(int, input().split()))

q = deque([i for i in range(1, n + 1)])
answer = 0

for i, j in enumerate(num):
    if q.index(j) > (n - i) // 2:
        while q[0] != j:
            q.appendleft(q.pop())
            answer += 1
        q.popleft()
    else:
        while q[0] != j:
            q.append(q.popleft())
            answer += 1
        q.popleft()
print(answer)
