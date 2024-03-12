tc = int(input())

tc_list = []

for i in range(tc):
    n, m = map(int, input().split())
    n_string = list(map(str, input().split()))
    m_string = list(map(str, input().split()))
    q = int(input())

    q_y = []
    answer = []
    for _ in range(q):
        a = int(input())
        answer.append(n_string[(a - 1) % n] + m_string[(a - 1) % m])
    ans = ' '.join(answer)
    print(f'#{i + 1} {ans}')
