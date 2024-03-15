import math

tc = int(input())

for i in range(tc):
    s, t = map(str, input().split())
    gcd = math.gcd(len(s), len(t))
    answer = ['yes', 'no']
    if s * (len(t) // gcd) == t * (len(s) // gcd):
        print(f'#{i + 1} {answer[0]}')
    else:
        print(f'#{i + 1} {answer[1]}')
