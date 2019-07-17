tc = int(input())
dp = [None for x in range(68)]
dp[0] = 1
dp[1] = 1
dp[2] = 2
dp[3] = 4


def calc_dp(i):
    if dp[i] is None:
        dp[i] = calc_dp(i - 1) + calc_dp(i - 2) + calc_dp(i - 3) + calc_dp(i - 4)

    return dp[i]


calc_dp(67)

for _ in range(tc):
    print(dp[int(input())])

