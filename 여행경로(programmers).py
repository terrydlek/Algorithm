'''
주어진 항공권을 모두 이용하여 여행경로를 짜려고 합니다. 항상 "ICN" 공항에서 출발합니다.
항공권 정보가 담긴 2차원 배열 tickets가 매개변수로 주어질 때, 방문하는 공항 경로를 배열에 담아 return 하도록 solution 함수를 작성해주세요.
제한사항
모든 공항은 알파벳 대문자 3글자로 이루어집니다.
주어진 공항 수는 3개 이상 10,000개 이하입니다.
tickets의 각 행 [a, b]는 a 공항에서 b 공항으로 가는 항공권이 있다는 의미입니다.
주어진 항공권은 모두 사용해야 합니다.
만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 합니다.
모든 도시를 방문할 수 없는 경우는 주어지지 않습니다.
'''
from collections import deque
n = int(input())
tickets = [list(map(str, input().split())) for _ in range(n)]


def solution(tickets):
    answer = []
    tk = sorted(tickets, key=lambda x:(x[0], x[1]))
    q = deque()
    q.append((["ICN"], tk)) # 이건 주서
    while q:
        # 현재 위치, 남은 티켓
        cur, tic = q.popleft()
        if tic.count(0) == len(tic):
            answer.append(cur)
            continue
        for i, j in enumerate(tic):
            if j != 0 and cur[-1] == j[0]:
                q.append((cur + [j[1]], tic[:i] + [0] + tic[i + 1:]))
    answer = answer[0]
    return answer


print(solution(tickets))

