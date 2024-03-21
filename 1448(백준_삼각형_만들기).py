import sys
n = int(sys.stdin.readline())
li = []
for i in range(n):
    li.append(int(sys.stdin.readline()))

li.sort(reverse=True)

for i in range(len(li) - 2):
    if li[i] < li[i + 1] + li[i + 2]:
        print(li[i] + li[i + 1] + li[i + 2])
        break
else:
    print(-1)
