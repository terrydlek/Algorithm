import sys
input = sys.stdin.readline

# 예약 손님 수
n = int(input())

reserve = []

for _ in range(n):
    reserve.append(list(map(str, input().strip().split())))


def solution(book_time):
    answer = []
    li = []
    for i in book_time:
        sh, sm = i[0].split(':')
        eh, em = i[1].split(':')
        start = int(sh) * 60 + int(sm)
        end = int(eh) * 60 + int(em) + 10
        li.append([start, end])
    li = sorted(li, key=lambda x: (x[0], x[1]))

    for i in li:
        if not answer:
            answer.append([i])
        else:
            for j in range(len(answer)):
                if answer[j][-1][-1] <= i[0]:
                    answer[j].append(i)
                    break
            else:
                answer.append([i])

    return len(answer)


print(solution(reserve))
