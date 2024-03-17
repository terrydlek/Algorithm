n = int(input())
std = []
for _ in range(n):
    std.append(''.join(reversed(input())))

cnt = 1

slc = []

while True:
    for i in std:
        if i[:cnt] in slc:
            break
        slc.append(i[:cnt])
    else:
        print(cnt)
        break
    cnt += 1
