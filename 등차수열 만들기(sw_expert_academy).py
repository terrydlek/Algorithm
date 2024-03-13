tc = int(input())

abc = [list(map(int, input().split())) for _ in range(tc)]

for i, j in enumerate(abc):
    print(f'#{i + 1} {abs((j[1] - (j[0] + j[2]) / 2))}')
