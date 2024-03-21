n = int(input())

word = [[input()] for _ in range(n)]
for i in range(n):
    word[i].append(len(word[i][0]))
    cnt = 0
    for j in word[i][0]:
        if j.isdigit():
            cnt += int(j)
    word[i].append(cnt)
word = sorted(word, key=lambda x: (x[1], x[2], x[0]))

for i in word:
    print(i[0])
