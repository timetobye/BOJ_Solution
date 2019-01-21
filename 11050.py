def get_binomial_coefficient(n, m):
    # dp is None
    dp = [[None for j in range(n+1)] for i in range(n+1)]

    for i in range(n+1):
        dp[i][i] = 1
        dp[i][0] = 1

    def calc_dp(y, x):
        # Pascal's triangle, dynamic programming with top-down method
        if dp[y][x] is None:
            dp[y][x] = calc_dp(y-1, x) + calc_dp(y-1, x-1)

        return dp[y][x]

    return calc_dp(n, m)


def main():
    n, k = map(int, input().split())
    print(get_binomial_coefficient(n, k))


if __name__ == "__main__":
    main()