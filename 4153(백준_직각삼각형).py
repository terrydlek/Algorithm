import sys
input = sys.stdin.readline

while True:
    avail = list(map(int, input().split()))
    if avail == [0, 0, 0]:
        break
    avail.sort()
    if avail[0]**2 + avail[1]**2 == avail[2]**2:
        print('right')
    else:
        print('wrong')
