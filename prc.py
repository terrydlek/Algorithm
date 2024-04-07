a, b = map(int, input().split())

prime_factors = [0] * (b + 1) #각 숫자의 소인수분해 값이 있는 변수. 문제에 의하면 숫자의 최대값이 b이므로 b+1까지 한다
for i in range(2, b + 1): #각 숫자의 소인수분해 값을 알아낸다(동적 계획법 적용)
    if not prime_factors[i]: #i값이 0이면 소인수분해 계산을 한다
            temp_num = i #먼저 i값을 임시로 저장한다
            while temp_num <= b + 1: #임시 저장한 i 값이 b이내에서 반복한다
                for j in range(temp_num, b + 1, temp_num): #j값은 temp_num의 배수로 b+1값 밑이라고 정의할 수 있다
                    prime_factors[j] += 1 #j(temp_num(i)의 배수) 소인수분해 개수를 1 증가한다
                temp_num *= i #temp_num은 i의 배수이다
            print(i, temp_num, prime_factors)
print(prime_factors)
#이제 a ~ b 범위에서 소인수분해 값이 소수인 숫자의 개수를 센다
result = 0
for i in range(a, b+1):
    if prime_factors[prime_factors[i]] == 1: #소인수분해개수[소인수분해개수[i(찾는값)]]. 소수는 소인수분해 개수가 1인점에 착안한다. 즉 i가 소수인지를 알려면 i의 소인수분해 개수의 소인수분해 개수가 1인지 알면 된다
        result += 1
print(result)
