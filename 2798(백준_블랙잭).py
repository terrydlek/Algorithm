import sys
from itertools import combinations as cb
input = sys.stdin.readline

n, m = map(int, input().split())
cards = list(map(int, input().split()))
answer = 0
for i in cb(cards, 3):
    if sum(i) <= m and answer < sum(i):
        answer = sum(i)
print(answer)
