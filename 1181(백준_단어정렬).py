n = int(input())
answer = []
for _ in range(n):
    string = input()
    answer.append(string)

answer = sorted(list(set(answer)), key=lambda x:(len(x), x))

for i in answer:
    print(i)
