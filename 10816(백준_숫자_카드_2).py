import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))

m = int(input())
cal = list(map(int, input().split()))

cnt = Counter(cards)

for i in cal:
    if i not in cnt:
        print(0, end=' ')
    else:
        print(cnt[i], end=' ')
