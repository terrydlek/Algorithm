import sys
from collections import defaultdict
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    clothes = defaultdict(int)
    for _ in range(n):
        string = input().strip().split()
        clothes[string[1]] += 1
    answer = 1
    for i in clothes:
        answer *= (clothes[i] + 1)
    print(answer - 1)
