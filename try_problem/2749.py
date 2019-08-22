import sys
sys.setrecursionlimit(100000000)

n = int(input())
dp = [None for i in range(n + 1)]
if n > 2:
    dp[0], dp[1] = 0, 1
else:
    dp = [0, 1]


def calc_dp(n):
    if dp[n] is None:
        dp[n] = calc_dp(n-1) % 1000000 + calc_dp(n-2) % 1000000

    return dp[n] % 1000000

print(calc_dp(n))