import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    repeat, string = map(str, input().strip().split())
    answer = ''
    for i in string:
        answer += i * int(repeat)
    print(answer)
