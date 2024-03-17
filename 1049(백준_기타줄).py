n, m = map(int, input().split())

avail = [list(map(int, input().split())) for _ in range(m)]

pac = sorted(avail, key=lambda x: x[0])[0][0]
ech = sorted(avail, key=lambda x: x[1])[0][1]

answer = min((n // 6) * pac + min((n % 6) * ech, pac), n * ech)
print(answer)
