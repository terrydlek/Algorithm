def solution(sequence, k):
    answer = []
    li = []
    start, end, tt = 0, 0, sequence[0]
    while end != len(sequence):
        if tt < k:
            if end == len(sequence) - 1:
                break
            else:
                end += 1
                tt += sequence[end]
        elif tt > k:
            tt -= sequence[start]
            start += 1
        else:
            li.append([start, end])
            end += 1
            tt += sequence[end]
        if start == end:
            break
    return answer


print(solution([2, 2, 2, 2, 2],	6))
