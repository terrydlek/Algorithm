import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    rank = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: x[0])
    doc = 1e9
    answer = 0
    for i in rank:
        if i[1] < doc:
            answer += 1
            doc = i[1]
    print(answer)
