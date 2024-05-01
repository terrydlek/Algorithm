import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
string = input().strip()

idx, cnt, answer = 0, 0, 0

while idx < (m - 1):
    if string[idx:idx + 3] == 'IOI':
        cnt += 1
        idx += 2
        if cnt == n:
            answer += 1
            cnt -= 1
    else:
        idx += 1
        cnt = 0
print(answer)
