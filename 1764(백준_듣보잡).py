import sys
input = sys.stdin.readline
n, m = map(int, input().split())

notlisten = set()
notsee = set()
for _ in range(n):
    name = input().strip()
    notlisten.add(name)

for _ in range(m):
    name = input().strip()
    notsee.add(name)

notls = sorted(notlisten.intersection(notsee))

print(len(notls))
for i in notls:
    print(i)
    