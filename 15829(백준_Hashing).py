import sys
input = sys.stdin.readline

l = int(input())
string = input().strip()

r, m = 31, 1234567891
answer = 0
for j, i in enumerate(string):
    answer += (ord(i) - 96) * r**j
print(answer % m)
