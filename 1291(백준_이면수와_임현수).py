n = int(input())


# 이면수
def lee(n):
    if n > 3 and n != 5:
        cnt = 0
        for i in str(n):
            cnt += int(i)
        if cnt % 2 == 1:
            return True
    return False


# 소인수분해
def factorization(n):
    num = n
    cnt = set()
    idx = 2
    while idx <= num:
        if num % idx == 0:
            num //= idx
            cnt.add(idx)
        else:
            idx += 1
    return cnt


# 합성수 (소수가 아닌 수)
def composite_number(n):
    if n >= 2:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return True
    return False


# 임현수
def im(n):
    # 2나 4라면
    if n in (2, 4):
        return True
    elif composite_number(n) and len(factorization(n)) % 2 == 0:
        return True
    return False


one = lee(n)
two = im(n)
if one and two:
    print('4')
elif one:
    print('1')
elif two:
    print('2')
else:
    print('3')
