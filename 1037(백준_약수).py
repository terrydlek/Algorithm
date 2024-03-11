r_c = int(input())
r_n = list(map(int, input().split()))

if len(r_n) == 1:
    print(r_n[0]**2)
else:
    print(max(r_n) * min(r_n))
