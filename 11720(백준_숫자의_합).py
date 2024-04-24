import sys
input = sys.stdin.readline

n = int(input())
num = input().strip()
answer = 0
for i in num:
    answer += int(i)
print(answer)
