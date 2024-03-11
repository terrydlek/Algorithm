import sys

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    n = str(n)
    if list(n) == list(reversed(n)):
        print('yes')
    else:
        print('no')
