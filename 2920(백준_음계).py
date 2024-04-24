import sys
input = sys.stdin.readline

avail = list(map(int, input().split()))

if avail == sorted(avail):
    print('ascending')
elif avail == sorted(avail, reverse=True):
    print('descending')
else:
    print('mixed')
