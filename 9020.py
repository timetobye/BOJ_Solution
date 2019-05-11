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
    res_prime_one, res_prime_two = 0, 0

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
