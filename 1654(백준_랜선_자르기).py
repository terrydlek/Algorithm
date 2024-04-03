import sys
input = sys.stdin.readline
k, n = map(int, input().split())

lan = [int(input()) for _ in range(k)]

start, end = 1, max(lan)
avail = []
def binary_search(target, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2
    count = 0
    for i in lan:
        count += i // mid

    if count >= n:
        avail.append(mid)
        start = mid + 1
    else:
        end = mid - 1
    return binary_search(target, start, end)


binary_search(k, start, end)
print(max(avail))
