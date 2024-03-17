n, sc, p = map(int, input().split())
score = []
if n != 0:
    score = list(map(int, input().split()))
score.append(sc)
rank = sorted(score, reverse=True)[:p]
rst = sorted(score, reverse=True)[p:]

if sc in rst:
    print(-1)
else:
    answer = []
    for i, j in enumerate(rank):
        if answer:
            if answer[-1][1] != j:
                answer.append([i + 1, j])
            else:
                answer.append([answer[-1][0], j])
        else:
            answer.append([i + 1, j])
        if j == sc:
            print(answer[-1][0])
            break
