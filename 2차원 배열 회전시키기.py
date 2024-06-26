li = [list(map(int, input().split())) for _ in range(3)]

def rotate(m, d):
    '''2차원 배열을 90도 단위로 회전해 반환.
    이 때 원 배열은 유지되며, 새로운 배열이 탄생한다. 이는 회전이 360도 단위일 때도 해당한다.
    2차원 배열은 행과 열의 수가 같은 정방형 배열이어야 한다.
    :input:
    m: 회전하고자 하는 2차원 배열. 입력이 정방형 행렬이라고 가정한다.
    d: 90도씩의 회전 단위. -1: 90도. 1: 90도, 2: 180도, 3: 270도, ...'''
    N = len(m)
    ret = [[0] * N for _ in range(N)]
    if d % 4 == 1:
        for r in range(N):
            for c in range(N):
                ret[c][N-1-r] = m[r][c]
    elif d % 4 == 2:
        for r in range(N):
            for c in range(N):
                ret[N-1-c][N-1-r] = m[r][c]
    elif d % 4 == 3:
        for r in range(N):
            for c in range(N):
                ret[N-1-c][r] = m[r][c]
    else:
        for r in range(N):
            for c in range(N):
                ret[r][c] = m[r][c]
    return ret

print(rotate(li, 1))