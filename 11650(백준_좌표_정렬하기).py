import sys
input = sys.stdin.readline

n = int(input())

avail = []

for _ in range(n):
    avail.append(list(map(int, input().split())))

avail = sorted(avail, key=lambda x:(x[0], x[1]))
for i in avail:
    print(f'{i[0]} {i[1]}')
