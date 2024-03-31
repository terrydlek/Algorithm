from collections import defaultdict
n = int(input())

words = [input() for _ in range(n)]
answer = 0
for i in range(n):
    for j in range(i + 1, n):
        fst, scd = words[i], words[j]
        dic = defaultdict(set)
        check = True
        for f, s in zip(fst, scd):
            dic[f].add(s)
            # dic[s].add(f)
            # print(dic, f, s)
            if len(dic[f]) > 1:
                # print(fst, scd, 1)
                break
            else:
                for k in dic:
                    if k != f and s in dic[k]:
                        check = False
                        break
        else:
            if check:
                answer += 1

print(answer)
