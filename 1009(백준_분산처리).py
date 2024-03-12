t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    dt_cnt = a**((b % 4) + 4) % 10
    if dt_cnt == 0:
        print(10)
    else:
        print(dt_cnt)
