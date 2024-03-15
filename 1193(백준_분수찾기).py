x = int(input())

prv, cur = 1, 1
add = 2
while cur < x:
    prv += 1
    cur += add
    add += 1

crt = add
for i in range(cur - prv + 1, cur + 1):
    add -= 1
    if i == x:
        break

if prv % 2 == 0:
    print(f'{crt - add}/{add}')
else:
    print(f'{add}/{crt - add}')
