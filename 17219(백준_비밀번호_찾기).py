import sys
input = sys.stdin.readline

n, m = map(int, input().split())
avail = dict()
for _ in range(n):
    domain, pswd = map(str, input().strip().split())
    avail[domain] = pswd

for _ in range(m):
    find = input().strip()
    print(avail[find])
