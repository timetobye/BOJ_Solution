"""
기본적인 피보나치 문제는 이걸로 풀어낼 수 있다.
"""

n = int(input())
dp = [None for _ in range(n+1)]
dp[0], dp[1] = [0, 1]


def calc_dp(n):
    if dp[n] is None:
        dp[n] = calc_dp(n-1) + calc_dp(n-2)

    return dp[n]


calc_dp(n)
print(dp[n])