ty, tm, td = map(int, input().split())
dy, dm, dd = map(int, input().split())


def isyoon(y):
    if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):
        return True
    return False

yoon = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
pyung = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

if (ty + 1000) + tm + td <= (dy + dm + dd):
    print('gg')
else:
    cnt = 0
    while (ty, tm, td) != (dy, dm, dd):
        td += 1
        if isyoon(ty):
            if yoon[tm] < td:
                td = 1
                tm += 1
                if tm > 12:
                    tm = 1
                    ty += 1
        else:
            if pyung[tm] < td:
                td = 1
                tm += 1
                if tm > 12:
                    tm = 1
                    ty += 1
        cnt += 1
    print('{}-{}'.format('D', cnt))
    