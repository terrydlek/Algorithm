import math
a, b = map(int, input().split())
c, d = map(int, input().split())

pi = a * d + c * b
di = b * d

gcd = math.gcd(pi, di)

print(pi // gcd, di // gcd)
