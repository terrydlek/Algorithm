n = int(input())
answer = 99
if n < 100:
    print(n)
else:
    for i in range(100, n + 1):
        string = str(i)
        diff = int(string[0]) - int(string[1])
        re = [int(string[0])]
        for j in range(1, len(string)):
            re.append(re[-1] - diff)
            if string[j] != str(re[-1]):
                break
        else:
            answer += 1
    print(answer)
