"""
bottom-up 방식으로 풀었습니다.
이 문제는 종이에 몇 줄 적어보면 피보나치 수열이라는 것을 알 수 있습니다.

원리는
N = 2 일 때 타일 상태에 00 을 붙이고,
N = 3 일 때 타일 상태에 1 을 붙이는 것 입니다.

즉, 현재 구해야 하는 단계의 값은 이전 두 단계 경우의 수 + 이전 한 단계의 경우의 수의 합 입니다.
"""
n = int(input())

dp = [1, 1, 2]

if n < 2:
    print(dp[n] % 15746)
else:
    for i in range(3, n + 1):
        value = dp[i - 2] + dp[i - 1]
        dp.append(value % 15746)

    print(dp[-1])


"""
legacy code
- 메모리 초과
"""
# import sys
# sys.setrecursionlimit(10000000)
#
# n = int(input())
#
#
# dp = [None for i in range(n + 1)]
# dp[0], dp[1], = 1, 1
#
#
# def calc_dp(n):
#     if dp[n] is None:
#         dp[n] = calc_dp(n-1) + calc_dp(n-2)
#
#     return dp[n] % 15746
#
#
# calc_dp(n)
print(dp[n])