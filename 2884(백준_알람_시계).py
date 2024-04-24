import sys
input = sys.stdin.readline

h, m = map(int, input().split())
time = h * 60 + m - 45

hour, minute = time // 60, time % 60
if hour < 0:
    hour = 24 + hour
print(f'{hour} {minute}')
