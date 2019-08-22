import sys
sys.setrecursionlimit(100000000)


def get_binomial_coefficient(n, m):
    # dp is None
    dp = [[None for j in range(n + 1)] for i in range(n + 1)]

    for i in range(n + 1):
        dp[i][i] = 1
        dp[i][0] = 1

    def calc_dp(y, x):
        if dp[y][x] is None:
            dp[y][x] = calc_dp(y-1, x) + calc_dp(y-1, x-1)

        return dp[y][x]

    return calc_dp(n, m)


while True:
    n, m = map(int, input().split())
    if (m == 0) and (n == 0):
        break
    else:
        result_value = get_binomial_coefficient(n, m)
        print(result_value)
