import sys
input = sys.stdin.readline

n = int(input())

cnt = 0
answer = 666

while cnt != n - 1:
    answer += 1
    if '666' in str(answer):
        cnt += 1

print(answer)
