t = int(input())


def distance(p1, p2, p3, p4):
    return ((p1 - p3)**2 + (p2 - p4)**2)**0.5


for _ in range(t):
    answer = 0
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    star = [list(map(int, input().split())) for _ in range(n)]
    for i in star:
        if distance(x1, y1, i[0], i[1]) < i[2] and distance(x2, y2, i[0], i[1]) > i[2]:
            answer += 1
        elif distance(x1, y1, i[0], i[1]) > i[2] and distance(x2, y2, i[0], i[1]) < i[2]:
            answer += 1
    print(answer)
