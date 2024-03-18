from collections import deque

n = int(input())
li = []
for _ in range(n):
    li.append(int(input()))
li.sort()

answer = 4
q = deque()
cnt = 0
for i in li:
    if not q:
        q.append(i)
        cnt += 1
    else:
        if i <= q[0] + 4:
            q.append(i)
            cnt += 1
            if cnt == 5:
                answer = 0
                break
        else:
            if answer > 5 - cnt:
                answer = 5 - cnt
            while q and q[0] + 4 < i:
                q.popleft()
            q.append(i)
            cnt = len(q)
if q:
    if answer > 5 - cnt:
        answer = 5 - cnt
print(answer)
