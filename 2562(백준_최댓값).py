import sys
input = sys.stdin.readline
avail = []
for _ in range(9):
    avail.append(int(input()))

print(max(avail))
print(avail.index(max(avail)) + 1)
