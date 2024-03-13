t = int(input())

tc = []
for _ in range(t):
    tc.append(int(input()))

for i, j in enumerate(tc):
    answer = 0
    for k in range(-j, j + 1):
        for l in range(-j, j + 1):
            if k**2 + l**2 <= j**2:
                answer += 1
    print(f'#{i + 1} {answer}')