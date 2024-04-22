t = int(input())

for tc in range(1, t + 1):
    n = list(input())
    minnum = n.copy()
    maxnum = n.copy()
    for i in range(len(n)):
        idx, mn = i, minnum[i]
        for j in range(i + 1, len(n)):
            if minnum[i] != minnum[j] and mn >= minnum[j]:
                if i == 0 and minnum[j] == '0':
                    continue
                mn = minnum[j]
                idx = j
        if (idx, mn) != (i, minnum[i]):
            minnum[i], minnum[idx] = minnum[idx], minnum[i]
            break
    minnum = ''.join(minnum)

    for i in range(len(n)):
        idx, mx = i, maxnum[i]
        for j in range(i + 1, len(n)):
            if maxnum[i] != maxnum[j] and mx <= maxnum[j]:
                mx = maxnum[j]
                idx = j
        if (idx, mx) != (i, n[i]):
            maxnum[i], maxnum[idx] = maxnum[idx], maxnum[i]
            break
    maxnum = ''.join(maxnum)
    print(f'#{tc} {minnum} {maxnum}')
