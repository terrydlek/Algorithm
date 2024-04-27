import sys
input = sys.stdin.readline

a, b, v = map(int, input().split())

answer = 1
v -= a
if v <= 0:
    print(answer)
else:
    progress = a - b
    if v / progress == v // progress:
        answer += v // progress
    else:
        answer += v // progress + 1
    print(answer)
    