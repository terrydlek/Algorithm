import sys
import heapq
input = sys.stdin.readline

v, e = map(int, input().split())
start = int(input())

grph = [[] for _ in range(v + 1)]
distance = [1e9] * (v + 1)

for _ in range(e):
    a, b, c = map(int, input().split())
    grph[a].append((b, c))


def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in grph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)
for i in distance[1:]:
    if i == 1e9:
        print('INF')
    else:
        print(i)
