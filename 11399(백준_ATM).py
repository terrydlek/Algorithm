import sys
import heapq
input = sys.stdin.readline

n = int(input())

time = list(map(int, input().split()))
heapq.heapify(time)
answer = 0
prv = 0
while time:
    a = heapq.heappop(time)
    answer += a + prv
    prv += a

print(answer)
