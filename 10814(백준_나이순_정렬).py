import sys
input = sys.stdin.readline

n = int(input())

member = []

for _ in range(n):
    a, b = map(str, input().strip().split())
    member.append([int(a), b])

member = sorted(member, key=lambda x:x[0])

for i in member:
    print(f'{i[0]} {i[1]}')
