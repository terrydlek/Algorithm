from itertools import combinations as cb
import math
avail = list(map(int, input().split()))
answer = 1e9
for i in list(cb(avail, 3)):
    cur = i[0]
    for j in i:
        cur = cur // math.gcd(cur, j) * j // math.gcd(cur, j) * math.gcd(cur, j)
    if answer > cur:
        answer = cur
print(answer)
