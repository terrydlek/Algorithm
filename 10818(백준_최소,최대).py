import sys
input = sys.stdin.readline

n = int(input())

avail = list(map(int, input().split()))
mn, mx = min(avail), max(avail)

print(f'{mn} {mx}')
