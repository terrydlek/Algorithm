n = int(input())
diff = []
for _ in range(n):
    a, b = map(int, input().split())
    diff.append(a - b)

diff.sort()

if n % 2 == 0:
    crt = n // 2
    print(diff[crt] - diff[crt - 1] + 1)
else:
    print(1)
