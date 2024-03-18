n = int(input())
name = []
for _ in range(n):
    name.append(input())

dic = {}
for i in name:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

ar = [[i, dic[i]] for i in dic]
ar = sorted(ar, key=lambda x: x[0])
ar = sorted(ar, key=lambda x: x[1], reverse=True)
print(ar[0][0])
