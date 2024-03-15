from itertools import combinations as cb

string = input()
li = [i for i in range(1, len(string) + 1)]

avail = []
for i in list(cb(li, 2)):
    if string[:i[0]] and string[i[0]:i[1]] and string[i[1]:]:
        st = ''.join(reversed(string[:i[0]])) + ''.join(reversed(string[i[0]:i[1]])) + ''.join(reversed(string[i[1]:]))
        avail.append(st)
avail = sorted(avail)
print(avail[0])