import sys
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())
grph = [[] for _ in range(n + 1)]
distance = [1e9] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    grph[a].append((b, c))
start, end = map(int, input().split())

def check(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in grph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


check(start)
print(distance[end])
