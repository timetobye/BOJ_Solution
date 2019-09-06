import sys
sys.setrecursionlimit(1000000)


def get_lcs_length(s1, s2):
    n = len(s1)
    m = len(s2)

    dp = [[None for i in range(n+1)] for j in range(m+1)]

    for j in range(m+1):
        for i in range(n+1):
            if j >= 1:
                dp[j][0] = 0
                continue
            dp[0][i] = 0

    def calc_dp(m, n):
        if dp[m][n] is None:
            dp[m][n] = max(calc_dp(m - 1, n), calc_dp(m, n - 1))
            if s1[n - 1] == s2[m - 1]:
                dp[m][n] = max(dp[m][n], calc_dp(m - 1, n - 1) + 1)

        return dp[m][n]

    return calc_dp(m, n)


def main():
    s1 = input()
    s2 = input()
    ret = get_lcs_length(s1, s2)
    print(ret)


if __name__ == "__main__":
    main()


"""
legacy code
# s1 = input()
# n = len(s1)
# s2 = input()
# m = len(s2)
# 
# dp = [[0 for i in range(len(s2)+1)] for x in range(len(s1)+1)]
# 
# for i in range(1, len(s1)+1):
#     for j in range(1, len(s2)+1):
#         print(dp)
#         dp[i][j] = max(dp[i-1][j], dp[i][j-1])
#         if s1[i-1] == s2[j-1]:
#             dp[i][j] = max(dp[i][j], dp[i-1][j-1]+1)
# print(dp)
# print(dp[n][m])
"""