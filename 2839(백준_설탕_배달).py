import sys
input = sys.stdin.readline

n = int(input())
answer = 0

while n != 0:
    if n % 5 != 0:
        n -= 3
        answer += 1
    else:
        answer += n // 5
        n = 0
    if n < 0:
        answer = -1
        break
print(answer)
