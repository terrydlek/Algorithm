# import sys
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
# tree = list(map(int, input().split()))
#
# start, end = 1, max(tree)
# answer = 0
#
#
# def binary_search(start, end):
#     global answer
#     if start > end:
#         return -1
#
#     mid = (start + end) // 2
#
#     total = 0
#     for i in tree:
#         if i > mid:
#             total += (i - mid)
#
#     if total >= m:
#         answer = mid
#         return binary_search(mid + 1, end)
#     else:
#         return binary_search(start, mid - 1)
#
#
# binary_search(start, end)
#
# print(answer)

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tree = list(map(int, input().split()))
start, end = 1, max(tree)

while start <= end:
    mid = (start + end) // 2
    total = 0
    for i in tree:
        if i > mid:
            total += (i - mid)
    if total >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)
