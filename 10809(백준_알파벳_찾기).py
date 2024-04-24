import sys
input = sys.stdin.readline

string = input().strip()

dic = {i: -1 for i in 'abcdefghijklmnopqrstuvwxyz'}

for i, j in enumerate(string):
    if dic[j] == -1:
        dic[j] = i

for i in dic:
    print(dic[i], end=' ')
