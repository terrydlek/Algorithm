n = int(input())
answer = 0
for _ in range(n):
    string = input()
    stack = []
    for i in string:
        if i not in stack:
            stack.append(i)
        else:
            if stack[-1] != i:
                break
            stack.append(i)
    else:
        answer += 1

print(answer)
