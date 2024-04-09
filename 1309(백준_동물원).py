n = int(input())

a, b = 1, 3

for _ in range(n - 1):
    a, b = b, (a + b * 2) % 9901

print(b)
