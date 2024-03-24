n = int(input())

a, b = 0, 1

for _ in range(abs(n) - 1):
    a, b = b % 1000000000, (a + b) % 1000000000

if n < 0 and abs(n) % 2 == 0:
    print(-1)
elif n == 0:
    print(0)
else:
    print(1)
if n == 0:
    print(0)
else:
    print(b % 1000000000)
