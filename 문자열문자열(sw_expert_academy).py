tc = int(input())

for i in range(tc):
    n = int(input())
    string = input()
    result = ['Yes', 'No']
    if n % 2 != 0:
        print(f'#{i + 1} {result[1]}')
    else:
        if string[:n//2] == string[n//2:]:
            print(f'#{i + 1} {result[0]}')
        else:
            print(f'#{i + 1} {result[1]}')
        