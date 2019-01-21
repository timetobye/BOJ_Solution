import sys
sys.setrecursionlimit(1000000)

n = int(input())
dp = [None for i in range(n+1)]
dp[0] = 0
if n > 0:
    dp[1] = 1


def calc_dp(n):
    if dp[n] is None:
        dp[n] = calc_dp(n-1) + calc_dp(n-2)

    return dp[n]


print(calc_dp(n))
