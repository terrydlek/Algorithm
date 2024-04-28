import sys
input = sys.stdin.readline

n = int(input())

paper = [list(map(int, input().split())) for _ in range(n)]
color = [0, 0]


def check(starty, startx, length):
    crt = paper[starty][startx]
    for i in range(starty, starty + length):
        for j in range(startx, startx + length):
            if paper[i][j] != crt:
                return False
    return True


def transfer(starty, startx, length):
    for i in range(starty, starty + length):
        for j in range(startx, startx + length):
            paper[i][j] = -1


while n != 1:
    for i in range(0, len(paper), n):
        for j in range(0, len(paper), n):
            if paper[i][j] != -1 and check(i, j, n):
                color[paper[i][j]] += 1
                transfer(i, j, n)
    n //= 2
for i in paper:
    for j in i:
        if j != -1:
            color[j] += 1

for i in color:
    print(i)
