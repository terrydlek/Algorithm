import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())

graph = []
for _ in range(n):
    graph.extend(list(map(int, input().split())))

time = [0] * 257

height = 0
# 높이를 하나씩 계산
for t in range(257):
    block = b
    for ground in graph:
        if t >= ground:
            block -= (t - ground)
            time[t] += (t - ground)
        else:
            block += (ground - t)
            time[t] += (ground - t) * 2
    if block >= 0 and height < t and time[height] >= time[t]:
        height = t
print(time[height], height)
