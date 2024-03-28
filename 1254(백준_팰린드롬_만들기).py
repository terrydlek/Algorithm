s = input()

start = len(s) // 2
answer = []
def pel(start):
    l1, l2 = start, start + 1
    ll1, ll2 = len(s[l1:]), len(s[l2:])
    if s[l1 - ll1:l1] == ''.join(reversed(s[l1:])):
        answer.append([ll1, 1])
        return True
    if s[l2 - 1 - ll2:l2 - 1] == ''.join(reversed(s[l2:])):
        answer.append([ll2, 2])
        return True
    return False


while start < len(s):
    pel(start)
    start += 1

answer = sorted(answer, key=lambda x:x[0], reverse=True)
if answer[0][1] == 1:
    print(len(s) * 2 - answer[0][0] * 2)
else:
    print(len(s) * 2 - (answer[0][0] * 2 + 1))
