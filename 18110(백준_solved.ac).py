import sys
input = sys.stdin.readline

def roundup(x):
    if x - int(x) >= 0.5:
        return int(x) + 1
    else:
        return int(x)

n = int(input())
opinion = []
for _ in range(n):
    opinion.append(int(input()))
opinion.sort()
julsa = roundup(len(opinion) * 0.15)

if julsa != 0:
    opinion = opinion[julsa:len(opinion) - julsa]

if len(opinion) == 0:
    print(0)
else:
    print(roundup(sum(opinion) / len(opinion)))
