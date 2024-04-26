import sys
input = sys.stdin.readline

n = int(input())
a = list(map(str, input().split()))

m = int(input())
b = list(map(str, input().split()))

a.sort()

def binary_search(target, data):
    start, end = 0, len(data) - 1
    while start <= end:
        mid = (start + end) // 2
        if data[mid] == target:
            print(1)
            return True
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    print(0)
    return False

for i in b:
    binary_search(i, a)
