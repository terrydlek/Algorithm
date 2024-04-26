import sys
from itertools import combinations as cb
input = sys.stdin.readline

n, k = map(int, input().split())

print(len(list(cb([0] * n, k))))
