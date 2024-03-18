# 스위치 개수
n = int(input())
# 스위치 상태
stat = list(map(int, input().split()))
stat = [0] + stat
# 학생 수
std = int(input())


# 여자 확인
def check(stat, num):
    cnt = 0
    cur = 1
    if num + cur >= len(stat) or num - cur == 0:
        return cnt
    while stat[num + cur] == stat[num - cur]:
        cnt += 1
        cur += 1
        if num + cur >= len(stat) or num - cur == 0:
            break
    return cnt


# 스위치 바꾸기
def change(stat, num):
    if stat[num] == 1:
        stat[num] = 0
    else:
        stat[num] = 1


# 학생의 성별, 학생이 받은 수
for _ in range(std):
    sx, num = map(int, input().split())
    if sx == 1:
        for i in range(num, len(stat), num):
            change(stat, i)
    else:
        rng = check(stat, num)
        if rng == 0:
            change(stat, num)
        else:
            for i in range(num - rng, num + rng + 1):
                change(stat, i)

for i, j in enumerate(stat[1:]):
    if (i + 1) % 20 == 0:
        print(j)
    else:
        print(j, end=' ')
