'''
점심시간에 도둑이 들어, 일부 학생이 체육복을 도난당했습니다. 다행히 여벌 체육복이 있는 학생이 이들에게 체육복을 빌려주려 합니다.
학생들의 번호는 체격 순으로 매겨져 있어, 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있습니다.
예를 들어, 4번 학생은 3번 학생이나 5번 학생에게만 체육복을 빌려줄 수 있습니다.
체육복이 없으면 수업을 들을 수 없기 때문에 체육복을 적절히 빌려 최대한 많은 학생이 체육수업을 들어야 합니다.
전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost,
여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때,
체육수업을 들을 수 있는 학생의 최댓값을 return 하도록 solution 함수를 작성해주세요.
'''
n = int(input())
lost = list(map(int, input().split()))
reserve = list(map(int, input().split()))


def solution(n, lost, reserve):
    answer = []
    lost.sort()
    for i in range(len(lost)):
        if lost[i] in reserve:
            answer.append(lost[i])
            reserve.remove(lost[i])
    for i in range(len(lost)):
        if lost[i] - 1 in reserve and lost[i] - 1 not in answer and lost[i] not in answer:
            answer.append(lost[i] - 1)
            reserve.remove(lost[i] - 1)
        elif lost[i] + 1 in reserve and lost[i] + 1 not in answer and lost[i] not in answer:
            answer.append(lost[i] + 1)
            reserve.remove(lost[i] + 1)
    return n - len(lost) + len(answer)


print(solution(n, lost, reserve))
