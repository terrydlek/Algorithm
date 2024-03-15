tc = int(input())

for i in range(tc):
    n = int(input())
    avail = []
    for j in range(1, int(n**0.5) + 1):
        if n % j == 0:
            avail.append(j + (n // j) - 2)
    print(f'#{i + 1} {min(avail)}')