import sys
input = sys.stdin.readline

n = int(input())
a = set()
for _ in range(n):
    cmd = input().strip().split()
    if cmd[0] == 'add':
        a.add(int(cmd[1]))
    elif cmd[0] == 'remove':
        a.discard(int(cmd[1]))
    elif cmd[0] == 'check':
        if int(cmd[1]) in a:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'toggle':
        if int(cmd[1]) in a:
            a.discard(int(cmd[1]))
        else:
            a.add(int(cmd[1]))
    elif cmd[0] == 'all':
        a = set([i for i in range(1, 21)])
    elif cmd[0] == 'empty':
        a = set()
