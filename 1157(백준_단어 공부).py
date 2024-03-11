from collections import Counter
string = input()

string = string.upper()

cnt = sorted(Counter(string).items(), key=lambda x:x[1], reverse=True)

mx = cnt[0][1]

count = 0

for i in cnt:
    if i[1] == mx:
        count += 1
    if count == 2:
        print('?')
        break
else:
    print(cnt[0][0])
