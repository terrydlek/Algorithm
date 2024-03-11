n = int(input())
li = []
answer = ''

# li에 문자열 넣기
for _ in range(n):
    li.append(input())

for i in range(len(li[0])):
    crt = li[0][i]
    for j in li:
        if j[i] != crt:
            answer += '?'
            break
    else:
        answer += li[0][i]

print(answer)
