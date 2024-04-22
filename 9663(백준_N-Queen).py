import sys
input = sys.stdin.readline

n = int(input())

row = [0] * (n)
answer = 0

# 퀸이 공격을 받는지 체크
def check(x):
    for i in range(x):
        # 같은 행에 퀸이 있거나 대각선에 퀸이 있는 경우
        if row[x] == row[i] or abs(row[i] - row[x]) == abs(x - i):
            return False
    return True


def dfs(start):
    global answer
    if start == n:
        answer += 1
    else:
        for i in range(n):
            row[start] = i
            if check(start):
                dfs(start + 1)


dfs(0)
print(answer)
