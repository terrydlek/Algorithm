n = int(input())
s = input()

miro = [['#'] * 101 for _ in range(101)]
miro[50][50] = '.'
idx = [50, 50]
avail = {'S': (1, 0), 'W': (0, -1), 'N': (-1, 0), 'E': (0, 1)}
dir = 'SWNE'

curdir = 0

for i in s:
    if i == 'R':
        curdir = (curdir + 1) % 4
    elif i == 'L':
        curdir -= 1
        if curdir < 0:
            curdir = 3
    else:
        idx[0] += avail[dir[curdir]][0]
        idx[1] += avail[dir[curdir]][1]
        miro[idx[0]][idx[1]] = '.'
miny, minx, maxy, maxx = 1e9, 1e9, 0, 0
for i in range(101):
    for j in range(101):
        if miro[i][j] == '.':
            if i < miny:
                miny = i
            if j < minx:
                minx = j
            if i > maxy:
                maxy = i
            if j > maxx:
                maxx = j

answer = []
for i in range(miny, maxy + 1):
    print(''.join(miro[i][minx:maxx + 1]))
