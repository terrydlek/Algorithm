import sys
input = sys.stdin.readline

n, m = map(int, input().split())

pkm = []
dic = {}
for i in range(1, n + 1):
    po = input().strip()
    pkm.append(po)
    dic[po] = i

for _ in range(m):
    string = input().strip()
    if string.isdigit():
        print(pkm[int(string) - 1])
    else:
        print(dic[string])
