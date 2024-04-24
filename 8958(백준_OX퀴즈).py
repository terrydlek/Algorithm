import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    string = input().strip()
    answer = 0
    cnt = 1
    status = 0
    for i in string:
        if i == 'O':
            if status == 1:
                cnt += 1
            answer += cnt
            status = 1
        else:
            cnt = 1
            status = 0
    print(answer)