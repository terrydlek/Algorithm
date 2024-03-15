tc = int(input())
answer = ['Alice', 'Bob']
for i in range(1, tc + 1):
    n = int(input())
    if n % 2 == 0:
        print(f'#{i} {answer[0]}')
    else:
        print(f'#{i} {answer[1]}')
