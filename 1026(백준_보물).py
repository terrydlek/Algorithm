n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a = sorted(a)
b = sorted(b, reverse=True)

answer = 0
for i, j in zip(a, b):
    answer += i * j

print(answer)
