'''
정수 n을 기준으로 n과 가까운 수부터 정렬하려고 합니다.
이때 n으로부터의 거리가 같다면 더 큰 수를 앞에 오도록 배치합니다.
정수가 담긴 배열 numlist와 정수 n이 주어질 때 numlist의 원소를 n으로부터 가까운 순서대로 정렬한 배열을 return하도록 solution 함수를 완성해주세요.
'''
numlist = list(map(int, input().split()))
n = int(input())


def solution(numlist, n):
    answer = []
    result = []
    for i in range(len(numlist)):
        answer.append(abs(numlist[i] - n))
    answer.sort()
    for j in range(len(answer)):
        if (answer[j] + n) in numlist and (answer[j] + n) not in result:
            result.append(answer[j] + n)
        else:
            result.append(abs(answer[j] - n))
    return result


print(solution(numlist, n))
