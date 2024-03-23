'''
검지, 중지, 약지일 때
다친 손가락 이용 횟수 짝수 : 5 + 4 * (n - 1) + hurt - 2
다친 손가락 이용 횟수 홀수 : 5 + 4 * (n - 1) + 4 - hurt

엄지일 때
8 * (hurt)

새끼일 때
20 + (hurt - 2) * 8
'''
hurt = int(input())
n = int(input())

if hurt in (2, 3, 4):
    if n % 2 == 0:
        print(5 + 4 * (n - 1) + hurt - 2)
    else:
        print(5 + 4 * (n - 1) + 4 - hurt)
elif hurt == 1:
    print(8 * n)
else:
    print(20 + (n - 2) * 8)
