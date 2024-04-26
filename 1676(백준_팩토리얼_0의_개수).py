import sys
import math

input = sys.stdin.readline
n = int(input())
num = str(math.factorial(n))

answer = 0

for i in range(len(num) - 1, -1, -1):
    if num[i] == '0':
        answer += 1
    else:
        break
print(answer)
