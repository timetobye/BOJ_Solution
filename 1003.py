tc = int(input())
for _ in range(tc):
    n = int(input())

    # n == 0일 경우 print(0, 1)
    if n == 0:
        print(1, 0)
        continue
    dp = [None for i in range(n+1)]
    dp[0] = 0
    dp[1] = 1

    # dp의 배열을 구하는 식
    def calc_dp(n):
        if dp[n] is None:
            dp[n] = calc_dp(n-1) + calc_dp(n-2)

        return dp[n]

    calc_dp(n)
    print(dp[n-1], dp[n])
