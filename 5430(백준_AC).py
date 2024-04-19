import sys
from collections import deque
input = sys.stdin.readline

t = int(input())


def transli(numli):
    string = ''
    li = []
    for i in numli:
        if i.isdigit():
            string += i
        else:
            if string:
                li.append(string)
                string = ''
    if string:
        li.append(string)
    return li


for _ in range(t):
    p = input().strip()
    n = int(input())
    num = input().strip()
    num = deque(transli(num))
    # print(num)

    # idx가 0이면 포인터는 제일 왼쪽, 1이면 제일 오른쪽
    idx = 0
    for i in p:
        if i == 'R':
            idx = (idx + 1) % 2
        else:
            if len(num) >= 1:
                if idx == 0:
                    num.popleft()
                else:
                    num.pop()
            else:
                print('error')
                break
    else:
        if idx == 1:
            answer = '[' + ','.join(list(reversed(num))) + ']'
            print(answer)
        else:
            answer = '[' + ','.join(list(num)) + ']'
            print(answer)
