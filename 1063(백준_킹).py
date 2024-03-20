# 킹 위치, 돌 위치, 움직이는 횟수
kidx, sidx, n = map(str, input().split())
move = []
for _ in range(int(n)):
    move.append(input())

col = {j: i + 1 for i, j in enumerate('ABCDEFGH')}
dir = {'R': (0, 1), 'L': (0, -1), 'B': (-1, 0), 'T': (1, 0), 'RT': (1, 1), 'LT': (1, -1), 'RB': (-1, 1), 'LB': (-1, -1)}
kcur, scur = [int(kidx[1]) - 1, col[kidx[0]] - 1], [int(sidx[1]) - 1, col[sidx[0]] - 1]

for i in move:
    movy, movx = dir[i][0], dir[i][1]
    if 0 <= kcur[0] + movy <= 7 and 0 <= kcur[1] + movx <= 7:
        if [kcur[0] + movy, kcur[1] + movx] != scur:
            kcur[0] += movy
            kcur[1] += movx
        else:
            if 0 <= scur[0] + movy <= 7 and 0 <= scur[1] + movx <= 7:
                kcur[0] += movy
                kcur[1] += movx
                scur[0] += movy
                scur[1] += movx

re = {i: j for i, j in enumerate('ABCDEFGH')}

print(re[kcur[1]] + str(kcur[0] + 1))
print(re[scur[1]] + str(scur[0] + 1))
