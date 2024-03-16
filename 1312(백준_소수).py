a, b, n = map(int, input().split())

cnt = 0
cur = -1

while cnt <= n:
    cur = a // b
    a = (a % b) * 10
    cnt += 1

print(cur)
