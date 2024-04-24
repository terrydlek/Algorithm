import sys
from collections import Counter
input = sys.stdin.readline
avail = []
for _ in range(10):
    avail.append(int(input()) % 42)

print(len(Counter(avail)))
