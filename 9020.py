"""
1. 소수 배열을 구한다. 0인 경우는 소수가 아니 것으로 설정
2. n = prime_lst[x] + prime_lst[n-x] 로 설정하면 모든 것을 순회하지 않고 조회 할 수 있다.
3. 이렇게 하면 시간 초과를 피할 수 있다.
4. prime_gap 는 임의로 크게 설정함
"""


from math import sqrt


def is_prime(num):
    if num > 1:
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True
    else:
        return False


test_case = int(input())
prime_lst = [0, 0]

for i in range(2, 10000 + 1):
    if is_prime(i):
        prime_lst.append(i)
    else:
        prime_lst.append(0)


for test in range(test_case):
    n = int(input())
    prime_gap = 100000**2

    for i, value in enumerate(prime_lst):
        if (value > 0) and (prime_lst[n-i] > 0):
            if value == (n - prime_lst[n-i]):
                if prime_gap > abs(value - prime_lst[n-i]):
                    res_prime_one, res_prime_two = value, prime_lst[n-i]
                    prime_gap = abs(value - prime_lst[n-i])

    print(res_prime_one, res_prime_two)


"""
legacy code

using combinations_with_replacement
-> time limit
"""


# for test in range(test_case):
#     n = int(input())
#
#     prime_gap = 100000**2
#     res_prime_one, res_prime_two = 0, 0
#     for i, j in combinations_with_replacement(prime_lst, 2):
#         if n == (i + j):
#             if prime_gap > abs(i-j):
#                 res_prime_one, res_prime_two = i, j
#
#     print(res_prime_one, res_prime_two)
