from collections import Counter
string = input()
cnt = Counter(string)
odd = 0
for i in cnt:
    if cnt[i] % 2 == 1:
        odd += 1
    if odd >= 2:
        break

if odd >= 2:
    print("I'm Sorry Hansoo")
else:
    li = sorted([[i, cnt[i]] for i in cnt], key=lambda x: x[0])
    od = ''
    answer = ''
    for i in li:
        if i[1] % 2 == 1:
            od = i[0]
        answer += (i[1] // 2) * i[0]
    answer = answer + od + ''.join(reversed(answer))
    print(answer)
