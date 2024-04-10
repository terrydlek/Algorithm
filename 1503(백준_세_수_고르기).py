n, m = map(int, input().split())

cant = list(map(int, input().split()))

answer = 1e9

for i in range(1, 1002):
    if i in cant:
        continue
    for j in range(1, 1002):
        if j in cant:
            continue
        for k in range(1, 1002):
            if k in cant:
                continue
            mul = i * j * k
            if abs(n - mul) < answer:
                answer = abs(n - mul)
            if n + 1 < mul:
                break
print(answer)
