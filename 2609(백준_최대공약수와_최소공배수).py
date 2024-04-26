import sys
import math
input = sys.stdin.readline

a, b = map(int, input().split())
gcd = math.gcd(a, b)
print(gcd)
print(a // gcd * b // gcd * gcd)
