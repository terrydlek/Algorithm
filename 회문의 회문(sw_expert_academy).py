t = int(input())

li = []
for _ in range(t):
    string = input()
    li.append(string)

def check_fst(string):
    if list(string) == list(reversed(string)):
        return True
    return False

def check_two(string):
    idx = (len(string) - 1) // 2
    if check_fst(string[:idx]) and check_fst(string[len(string) - idx:]):
        return True
    return False


for i, j in enumerate(li):
    if check_fst(j) and check_two(j):
        print('#{} YES'.format(i + 1))
    else:
        print('#{} NO'.format(i + 1))
