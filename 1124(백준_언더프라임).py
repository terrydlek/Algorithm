import math
a, b = map(int, input().split())

prime = [True for _ in range(b + 1)]
prime[1] = False
for i in range(2, b + 1):
    if not prime[i]:
        continue
    for j in range(i * i, b + 1, i):
        prime[j] = False


def decom(num):
    cnt = 0
    for i in range(2, int(math.sqrt(num)) + 1):
        while num % i == 0:
            cnt += 1
            num //= i

    if num != 1:
        cnt += 1
    return cnt


answer = 0
for i in range(a, b + 1):
    if prime[decom(i)]:
        answer += 1

print(answer)
