n = int(input())

n = str(n)

answer = 1
cur = ''
if len(n) == 1:
    cur = '0' + n
    cur = cur[-1] + str((int(cur[0]) + int(cur[1])))[-1]
else:
    cur = n[-1] + str((int(n[0]) + int(n[1])))[-1]

while int(cur) != int(n):
    answer += 1
    if len(cur) == 1:
        cur = '0' + n
    cur = cur[-1] + str((int(cur[0]) + int(cur[1])))[-1]

print(answer)
