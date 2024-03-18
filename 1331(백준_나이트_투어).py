rte = []
for _ in range(36):
    rte.append(input())

col = {i: j for i, j in zip('ABCDEF', [1, 2, 3, 4, 5, 6])}
row = [str(i) for i in range(1, 6 + 1)]

if len(set(rte)) != len(rte):
    print('Invalid')
else:
    avail = [(2, -1), (2, 1), (-2, -1), (-2, 1), (1, -2), (1, 2), (-1, -2), (-1, 2)]
    y, x = 0, 0
    for i, j in enumerate(rte):
        if i == 0:
            y, x = col[j[0]], int(j[1])
        elif i == 35:
            if (col[rte[0][0]] - col[j[0]], int(rte[0][1]) - int(j[1])) not in avail:
                print('Invalid')
                break
        else:
            if (y - col[j[0]], x - int(j[1])) in avail:
                y, x = col[j[0]], int(j[1])
            else:
                print('Invalid')
                break
    else:
        print('Valid')
