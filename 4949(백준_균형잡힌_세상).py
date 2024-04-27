while True:
    string = input()
    if string == '.':
        break
    stack = []
    for i in string:
        if i in '([':
            stack.append(i)
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                print('no')
                break
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                print('no')
                break
    else:
        if not stack:
            print('yes')
        else:
            print('no')
