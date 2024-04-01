s, k = map(int, input().split())

avail = [s // k for _ in range(k)]
for i in range(s % k):
    avail[i] += 1
answer = 1
for i in avail:
    answer *= i

print(answer)
