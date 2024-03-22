num = input()

answer = 0
idx = 0

while True:
    answer += 1
    for i in str(answer):
        if i == num[idx]:
            idx += 1
            if idx >= len(num):
                print(answer)
                exit()
