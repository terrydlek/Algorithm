from collections import Counter
n = int(input())

for _ in range(n):
    area = list(map(int, input().split()))
    mx = Counter(area).most_common(1)[0]
    if len(area) % 2 == 0:
        if mx[1] >= len(area) // 2:
            print(mx[0])
        else:
            print('SYJKGW')
    else:
        if mx[1] > len(area) // 2:
            print(mx[0])
        else:
            print('SYJKGW')
