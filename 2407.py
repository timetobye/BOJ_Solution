m, n = map(int, input().split())


# pascal's triangle default arr
dp = [[None for i in range(m+1)] for j in range(m+1)]
for j in range(m+1):
    for i in range(m+1):
        dp[j][0] = 1
        if j == i:
            dp[j][i] = 1


# top-down method
def calc_dp(m, n):
    if dp[m][n] is None:
        dp[m][n] = calc_dp(m-1, n) + calc_dp(m-1, n-1)

    return dp[m][n]


print(calc_dp(m, n))