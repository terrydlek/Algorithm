import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())

dic = {str(i): 0 for i in range(10)}
for i in str(a * b * c):
    dic[i] += 1

for i in dic:
    print(dic[i])
    