string = input()
number, sign = [], []
num = ''
for i in string:
    if i.isdigit():
        num += i
    else:
        number.append(int(num))
        sign.append(i)
        num = ''
number.append(int(num))

answer = number[0]
number = number[1:len(number)]
prv = 'plus'
for i, j in zip(number, sign):
    if prv == 'minus':
        if j == '+':
            answer -= i
        else:
            answer -= i
            # prv = 'plus'
    else:
        if j == '+':
            answer += i
        else:
            answer -= i
            prv = 'minus'
print(answer)
