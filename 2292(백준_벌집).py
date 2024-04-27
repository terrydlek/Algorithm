import sys
input = sys.stdin.readline

n = int(input())

'''
1 - 7 - 19 - 37 - 61 - ... ( 6 - 12 - 18 - 24 ...)
'''
answer = 1
cnt = 1
plus = 6
while cnt < n:
    cnt += plus
    plus += 6
    answer += 1
print(answer)
